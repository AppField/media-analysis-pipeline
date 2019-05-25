from bs4 import BeautifulSoup
import urllib.request
import re
import sys
import json
import logging


def get_soup(url):
    page = urllib.request.urlopen(url)
    return BeautifulSoup(page, 'html.parser')   

def query_article(url):
    return get_soup(url)
    
    
def build_datadoc(soup):
    # get published year and month to create folder hierarchy
    article_published = soup.find('meta', attrs={'name': 'krn:published_time'})['content']
    published = article_published[:7]
    # get article id and modified to save different versions
    article_id = soup.find('meta', attrs={'name': 'krn-article-id'})['content']
    article_modified = soup.find('meta', attrs={'name': 'krn-article-modified'})['content']
    
    if article_id != None:
        return {
            "directory": 'krone/{0}/'.format(published), 
            "filename": '{0}_{1}.json'.format(article_id, article_modified),
            'content': str(soup)
        }
    else:
        raise Exception("No Article found")
    

def main():
    #log_filename = '/src/krone/debug.log'
    #logging.basicConfig(filename = log_filename, level=logging.DEBUG)
    
    url = sys.stdin.readline()
    #url = 'https://www.krone.at/1928845'
    
    datadoc = build_datadoc(query_article(url))
    print(json.dumps(datadoc))


if __name__ == "__main__":
    main()


