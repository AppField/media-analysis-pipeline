from bs4 import BeautifulSoup
import urllib.request
from base_transformer import Transformer
import json

class KroneTransformer(Transformer):

    meta_data = [
        {'prop': 'name', 'value': 'krn:published_time'},
        {'prop': 'name', 'value': 'krn:modified_time'},
        {'prop': 'property', 'value': 'og:url'},
        {'prop': 'property', 'value': 'og:title'},
    ]

    def get_article_id(self):
        return self.get_meta_content({'prop': 'name', 'value': 'krn-article-id'})

    def get_ressorts(self):
        ressort_hierarchical = self.soup.find(
            'meta', {'name': 'krn-ressort-slug_hierarchical'})['content']
        ressorts_text = ressort_hierarchical.split('/')
        if ressorts_text.__len__() > 0:
            ressorts = {
                'name': ressorts_text[0]
            }
            ressorts = self.get_subressort(ressorts, ressorts_text[1:])
            return ressorts
        else:
            return None

    def get_subressort(self, ressorts, ressorts_text):
        if ressorts_text.__len__() > 0:
            subressort = {
                'name': ressorts_text[0]
            }
            self.get_subressort(subressort, ressorts_text[1:])
            ressorts['subressort'] = subressort
            return ressorts
        else:
            return ressorts

    # Note: Some articles don't have an author
    def get_author(self):
        content = self.soup.find('div', {'class': 'c_content'})
        boxes = content.find_all('div', {'class': 'box'})
        last_box = boxes[boxes.__len__() - 1]
        
        p = last_box.find('p', {'style': 'text-align: right;'})
        if p != None:
            em = p.find('em')
            if em != None:
                return em.text.strip().replace(', Kronen Zeitung', '')
    
        # Take standard author line. Mostly krone.at or krone Sport
        div = self.soup.find('div', {'class': 'authorline__name'})
        return div.text.strip() if div != None else None

    def are_comments_allowed(self):
        comments = self.soup.find(
            'em', text='Die Kommentarfunktion wurde bis auf Weiteres deaktiviert.')
        return comments == None

    def get_tags(self):
        tags_body = self.soup.find(
            'div', {'class': 'retresco-story-tags__body'})
        if tags_body != None:
            tags = tags_body.find_all('a')
            return [tag.text for tag in tags]
        return []

    def get_article_text(self):
        box = self.soup('div', {'class': 'kmm-article-box'})
        if box != None:
            paragraphs = box[0].find_all('p')
            texts = [p.text for p in paragraphs]
            return ' '.join(texts)
        return None

def main():
    html = urllib.request.urlopen(
        'https://www.krone.at/1945872')

    datadoc = KroneTransformer(html).extract_data()
    print(json.dumps(datadoc))


if __name__ == "__main__":
    main()