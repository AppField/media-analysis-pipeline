from bs4 import BeautifulSoup
import urllib.request
from base_extractor import Extractor
import re


class UnzensuriertExtractor(Extractor):

    meta_data = [
        {'prop': 'property', 'value': 'article:published_time'},
        {'prop': 'property', 'value': 'article:modified_time'},
        {'prop': 'property', 'value': 'og:url'},
        {'prop': 'property', 'value': 'og:title'},
    ]

    def get_article_id(self):
        url = self.soup.find('meta', {'property': 'og:url'})['content']
        return re.compile('[0-9]+').findall(url)[0]

    def get_ressorts(self):
        return {'name': self.soup.find('meta', {'name': 'keywords'})['content']}

    # Note: Some articles don't have an author
    def get_author(self):
        return self.soup.find('meta', {'property': 'article:author'})['content']

    def are_comments_allowed(self):
        comments = self.soup.find('p', {'class': 'comment-write-login'})
        return comments == None

    def get_tags(self):
        tags_body = self.soup.find(
            'div', {'class': 'retresco-story-tags__body'})
        if tags_body != None:
            tags = tags_body.find_all('a')
            return [tag.text for tag in tags]
        return []

    def get_article_text(self):
        box = self.soup('div', {'id': 'content-inner'})
        if box != None:
            paragraphs = box[0].find_all('p')
            texts = [p.text for p in paragraphs]
            return ' '.join(texts)
        return None
