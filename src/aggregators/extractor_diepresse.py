from bs4 import BeautifulSoup
import urllib.request
from base_extractor import Extractor
import urllib.request


class DiePresseExtractor(Extractor):

    meta_data = [
        {'prop': 'property', 'value': 'article:published_time'},
        {'prop': 'property', 'value': 'article:modified_time'},
        {'prop': 'property', 'value': 'og:url'},
        {'prop': 'property', 'value': 'og:title'}
    ]

    def get_article_id(self):
        return self.get_meta_content({'prop': 'name', 'value': 'oct:articleID'})

    def get_ressorts(self):
        ul = self.soup.find('ul', {'class': 'breadcrumbs__menu'})
        ressorts_text = [anchor.text for anchor in ul.find_all(
            'a', {'class': 'breadcrumbs__link'})]
        if ressorts_text.__len__() > 1:
            ressorts = {
                'name': ressorts_text[1]
            }
            ressorts = self.get_subressort(ressorts, ressorts_text[2:])
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
        anchor = self.soup.find('a', {'class': 'article__author'})
        return anchor.text.replace('von', '').strip() if anchor != None else None

    def are_comments_allowed(self):
        comments = self.soup.find('section', {'class': 'comments'})
        return comments != None

    def get_article_text(self):
        article = self.soup('article', {'class': 'article'})
        if article != None:
            paragraphs = article[0].find_all('p')
            texts = [p.text.replace('\n', '').strip() for p in paragraphs]
            return ' '.join(texts)
        return None

    def is_plus(self):
        plus_banner = self.soup.find('span', {'class': 'plus-banner'})
        return plus_banner != None

def main():
    html = urllib.request.urlopen(
        'https://diepresse.com/home/innenpolitik/5643381/Freies-Spiel-der-Kraefte_Antragsflut-im-Nationalrat')

    DiePresseExtractor(html).extract_data()


if __name__ == "__main__":
    main()