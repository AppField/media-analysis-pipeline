from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re


def get_soup(url):
    req = Request(url,
                  headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req)
    return BeautifulSoup(page, 'html.parser')


def query_newsfeed():

    base_url = 'https://www.unzensuriert.at'
    url = 'https://www.unzensuriert.at/neu'
    soup = get_soup(url)

    items = soup.find('div', {'class': 'item-list'}
                      ).find_all('li', {'class': 'views-row'})

    links = ['{0}{1}'.format(base_url, item.find('a')['href'])
             for item in items]

    print('\n'.join(links))


def main():
    query_newsfeed()


if __name__ == "__main__":
    main()
