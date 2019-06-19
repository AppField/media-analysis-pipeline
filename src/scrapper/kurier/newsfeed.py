from bs4 import BeautifulSoup
import urllib.request
import re
import os
import sys
# Necessary to let python find base_newsfeed
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from base_newsfeed import Newsfeed

class KurierNewsfeed(Newsfeed):   
    directory= 'kurier'
    
    def query_newsfeed(self):
        top_topics = self.soup.find('section', {'class': 'topTopics'})
            
        articles = top_topics.find_all('a', { 'class': 'teaser-title'})    

        self.links = [ '{0}{1}'.format(self.url, article['href'].strip()) for article in articles ]

def main():
    KurierNewsfeed('http://kurier.at')

if __name__ == "__main__":
    main()