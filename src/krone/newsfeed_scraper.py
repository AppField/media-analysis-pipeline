from bs4 import BeautifulSoup
import urllib.request
import re
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))


def get_soup(url):
    page = urllib.request.urlopen(url)
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
    url = 'https://www.krone.at/'
    soup = get_soup(url)

    items = soup.find_all('div', {'class': 'newsticker__item'})
    links = [item.find('a')['href'] for item in items]

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
