from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import sys
import json
import os
# Necessary to let python find base_article
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from base_article import BaseArticle

class DiePresseArticle(BaseArticle):
    magazine = 'diepresse'    
    
    def set_meta_data(self):
        self.article_id = self.soup.find('meta', attrs={'name': 'oct:articleID'})['content']

        # get published year and month to create folder hierarchy
        self.article_published = self.soup.find('meta', attrs={'property': 'article:published_time'})['content']
        
        # get modified to save different versions
        self.article_modified = self.soup.find('meta', attrs={'property': 'article:modified_time'})['content']

def main():
    url = sys.stdin.readline()    
    article = DiePresseArticle(url)
    datadoc = article.build_datadoc()
    print(json.dumps(datadoc))


if __name__ == "__main__":
    main()