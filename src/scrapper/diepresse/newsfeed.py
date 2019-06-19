from bs4 import BeautifulSoup
import urllib.request
import re
import os
import sys
# Necessary to let python find base_newsfeed
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from base_newsfeed import Newsfeed

class DiePresseNewsfeed(Newsfeed):
    directory = 'diepresse'

    def query_newsfeed(self):
        items = self.soup.find('ul', {'class': 'ticker__list'}).find_all('li', {'class': 'ticker__item'})        
        
        base_url = 'https://diepresse.com'
        self. links = ['{0}{1}'.format(base_url, item.find('a')['href']) for item in items]        

def main():
    DiePresseNewsfeed('https://diepresse.com/home/newsticker/index.do')

if __name__ == "__main__":
    main()