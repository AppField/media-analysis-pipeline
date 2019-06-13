from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import sys
import json
import logging
import re

class BaseArticle():
    article_id = ''
    article_published = ''
    article_modified = ''
    magazine = ''    

    def __init__(self, url):
        self.url = url
        self.soup = self.get_soup(url)
        self.set_meta_data()

    def get_soup(self, url):
        req = Request(url,
                      headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(req)
        return BeautifulSoup(page, 'html.parser')

    def set_meta_data(self):
        pass        

    def build_datadoc(self):     

        article_published = self.article_published[:7]
     
        # Replace colon with %3A due to HDFS not allowing filenames with colons
        article_modified = self.article_modified.replace(':', '%3A')

        if self.article_id != None:
            return {
                'id': self.article_id,
                'magazine': self.magazine,
                "directory": '{0}/{1}'.format(self.magazine, '/'.join(article_published.split('-'))),
                "filename": '{0}_{1}.json'.format(self.article_id, article_modified),
                'content': str(self.soup)
            }
        else:
            raise Exception("No Article found")
