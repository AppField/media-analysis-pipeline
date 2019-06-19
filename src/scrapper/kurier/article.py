from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import sys
import json
import os
import datetime

# Necessary to let python find base_article
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from base_article import BaseArticle

class KurierArticle(BaseArticle):
    magazine = 'kurier'

    def set_meta_data(self):        
        self.article_id = re.search('[0-9]+', self.url).group()

        # get published year and month to create folder hierarchy        
        published_date = self.soup.find('div', {'class': 'article-header-intro-right'})
        if published_date != None:
            date = published_date.find('span').text.strip()
            format_str = '%m/%d/%Y'
            self.article_published =  str(datetime.datetime.strptime(date, format_str))            
        else:
            self.article_published = datetime.datetime.now()

        
        
        # get modified to save different versions
        meta_date = self.soup.find('span', {'class': 'article-meta-date'})
        if meta_date != None:
            date = meta_date.text.replace('Stand:', '').strip()
            format_str = '%m/%d/%Y, %H:%M'

            self.article_modified = str(datetime.datetime.strptime(date, format_str))
        else:
            self.article_modified = datetime.datetime.now()
    

def main():
    #url = 'https://kurier.at/wirtschaft/wir-haben-uns-mit-den-sanktionen-selbst-ins-knie-geschossen/400521760'
    url = sys.stdin.readline()
    article = KurierArticle(url)
    datadoc = article.build_datadoc()
    print(json.dumps(datadoc))


if __name__ == "__main__":
    main()