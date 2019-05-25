from bs4 import BeautifulSoup
import urllib.request
import re

def get_soup(url):
        page = urllib.request.urlopen(url)
        return BeautifulSoup(page, 'html.parser')

def query_newsfeed():
    url = 'https://www.krone.at/'
    soup = get_soup(url)

    items = soup.find_all('div', {'class': 'newsticker__item'})
            
    links = [ item.find('a')['href'] for item in items ]    

    print('\n'.join(links)) 

def main():
    query_newsfeed()

if __name__ == "__main__":
    main()


