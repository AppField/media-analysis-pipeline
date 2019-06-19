from bs4 import BeautifulSoup
import urllib.request
from base_transformer import Transformer
import re

class SnTransformer(Transformer):

    meta_data = [        
        {'prop': 'property', 'value': 'og:article:published_time'},
        {'prop': 'property', 'value': 'og:article:modified_time'},
        {'prop': 'property', 'value': 'og:url'},
        {'prop': 'property', 'value': 'og:title'},
    ]

    def get_article_id(self):
        url = self.soup.find('meta', {'property': 'og:url'})['content']
        return re.compile('[0-9]*$').findall(url)[0]

    def get_ressorts(self):
        ressort_hierarchical = self.soup.find('meta', {'property': 'og:url'})['content'].split('/')
        ressorts_text = ressort_hierarchical[3:ressort_hierarchical.__len__() - 1]        
        if ressorts_text.__len__() > 0:
            ressorts = {
                'name': ressorts_text[0]
            }
            ressorts = self.get_subressort(ressorts, ressorts_text[1:])            
            return ressorts
        else: return None

    def get_subressort(self, ressorts, ressorts_text):
        if ressorts_text.__len__() > 0:            
            subressort = {
                'name': ressorts_text[0]
            }
            self.get_subressort(subressort, ressorts_text[1:])
            ressorts['subressort'] = subressort
            return ressorts
        else: return ressorts

    # Note: Some articles don't have an author
    def get_author(self):
        author_box = self.soup.find('p', { 'itemprop': 'author'})
        if author_box != None:
            return author_box.find('a').text.strip()
        else: return None        

    def are_comments_allowed(self):
        comments = self.soup.find('button', {'class': 'comments__adder'})
        return comments != None

    def get_tags(self):
        tags_body = self.soup.find('div', {'class': 'wrap-tags'})
        if tags_body != None:
            tags = tags_body.find_all('a')
            return [ tag.text.strip() for tag in tags]
        return []
    
    def get_article_text(self):        
        box = self.soup.find('div', {'class': 'article__body'})
        if box != None:
            paragraphs = box.find_all('p')
            texts = [ p.text.strip() for p in paragraphs ]
            return ' '.join(texts)
        return None                         

    def is_plus(self):
        premium_boxes = self.soup.find_all('span', {'class': 'article__premium'})
        return premium_boxes.__len__() > 0

def main():
    url = 'https://www.sn.at/politik/weltpolitik/us-praesident-trump-trifft-britische-premierministerin-may-71236891'
    #url = 'https://www.sn.at/salzburg/wirtschaft/mittags-billig-abends-teuer-koennen-flexible-preise-die-touristenstroeme-lenken-71223766'
    SnTransformer(url)

if __name__ == "__main__":
    main()