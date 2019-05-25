from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import sys
import json
import logging
import re


def get_soup(url):
    req = Request(url,
                  headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req)
    return BeautifulSoup(page, 'html.parser')


def query_article(url):
    return get_soup(url)


def get_article_id(url):
    return re.search('[0-9]+', url).group()


def build_datadoc(soup, article_id):
    # get published year and month to create folder hierarchy
    article_published = soup.find(
        'meta', attrs={'property': 'article:published_time'})['content']
    published = article_published[:7]
    # get modified to save different versions
    article_modified = soup.find(
        'meta', attrs={'property': 'article:modified_time'})['content']

    if article_id != None:
        return {
            "directory": 'unzensuriert/{0}/'.format(published),
            "filename": '{0}_{1}.json'.format(article_id, article_modified),
            'content': str(soup)
        }
    else:
        raise Exception("No Article found")


def main():

    url = sys.stdin.readline()
    datadoc = build_datadoc(query_article(url), get_article_id(url))
    print(json.dumps(datadoc))


if __name__ == "__main__":
    main()
