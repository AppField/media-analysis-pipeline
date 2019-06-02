from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))


def get_soup(url):
    req = Request(url,
                  headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req)
    return BeautifulSoup(page, 'html.parser')


def read_last_url():
    filename = os.path.join(THIS_FOLDER, 'last_url.txt')
    file = open(filename, "r")
    url = file.read()
    file.close
    return url


def save_last_url(url):
    filename = os.path.join(THIS_FOLDER, 'last_url.txt')
    file = open(filename, "w+")
    file.write(url)
    file.close()


def query_newsfeed():

    base_url = 'https://www.unzensuriert.at'
    url = 'https://www.unzensuriert.at/neu'
    soup = get_soup(url)

    items = soup.find('div', {'class': 'item-list'}
                      ).find_all('li', {'class': 'views-row'})

    links = ['{0}{1}'.format(base_url, item.find('a')['href'])
             for item in items]

    # Get and Save last scrapped article URL to only print newly added URLs
    last_url = read_last_url()

    i = 0
    while i < links.__len__() and links[i] != last_url:
        print('{}'.format(links[i]))
        i += 1

    save_last_url(links[0])


def main():
    query_newsfeed()


if __name__ == "__main__":
    main()
