from bs4 import BeautifulSoup
import urllib.request
import re
import os
import sys
# Necessary to let python find base_newsfeed
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from base_newsfeed import Newsfeed

class UnzensuriertNewsfeed(Newsfeed):
    directory = 'unzensuriert'

    def query_newsfeed(self):
        items = self.soup.find('div', {'class': 'item-list'}).find_all('li', {'class': 'views-row'})

        base_url = 'https://unzensuriert.at'
        self.links = ['{0}{1}'.format(base_url, item.find('a')['href']) for item in items]

def main():
    UnzensuriertNewsfeed('http://unzensuriert.at/neu')

if __name__ == "__main__":
    main()