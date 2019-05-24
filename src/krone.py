from bs4 import BeautifulSoup
import urllib.request
import re

class Article_Scraper():
    url = 'https://www.krone.at/'

    def get_soup(self, url):
        page = urllib.request.urlopen(url)
        return BeautifulSoup(page, 'html.parser')

    def get_articles(self):
        try:
            soup = self.get_soup(url)    
            
            items = soup.find_all('div', {'class': 'newsticker__item'})
            
            links = [ item.find('a')['href'] for item in items ]    
                    
            for link in links:
                yield self.get_soup(link)           
            
        except:
            print("An error occured.")



Article_Scraper()

