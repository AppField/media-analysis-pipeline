from bs4 import BeautifulSoup
import urllib.request
import re

def get_soup(url):
        page = urllib.request.urlopen(url)
        return BeautifulSoup(page, 'html.parser')

def query_newsfeed():

    base_url = 'https://diepresse.com'
    url = 'https://diepresse.com/home/newsticker/index.do'
    soup = get_soup(url)

    items = soup.find('ul', {'class': 'ticker__list'}).find_all('li', {'class': 'ticker__item'})
    
    links = [ '{0}{1}'.format(base_url, item.find('a')['href']) for item in items ]    

    print('\n'.join(links)) 

def main():
    query_newsfeed()

if __name__ == "__main__":
    main()


