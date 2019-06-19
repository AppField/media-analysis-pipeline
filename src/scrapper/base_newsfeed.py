from bs4 import BeautifulSoup
import urllib.request
import re
import os


class Newsfeed():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    directory = ''    
    links = [] #array of articles links.Needs to be filled in query_newsfeed function()

    def __init__(self, url):  
        self.last_url_dirname = os.path.join(self.THIS_FOLDER, self.directory, 'last_url.txt')
        self.url = url      
        self.soup = self.get_soup(url)
        self.query_newsfeed()
        self.write_links()

    def get_soup(self, url):
        req = urllib.request.Request(url = url, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        })
        html = urllib.request.urlopen(req)
        return BeautifulSoup(html, 'html.parser')

    def query_newsfeed(self):
        pass

    def write_links(self):       
        
        file = open(self.last_url_dirname, 'r+')

        last_url = file.read()
        i = 0
        while i < self.links.__len__() and self.links[i] != last_url:
            print(self.links[i])
            i += 1
        
        file.close()
        file = open(self.last_url_dirname, 'w+') # close and open it in w mode to override content
        if self.links.__len__() > 0:
            file.write(self.links[0])
        file.close()