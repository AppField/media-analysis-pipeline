from bs4 import BeautifulSoup
import urllib.request

class Extractor():
    # change prop and value attributes in subclasses
    meta_data = [
        {'prop': 'name', 'value': 'krn-article-id'},
        {'prop': 'name', 'value': 'krn:published_time'},
        {'prop': 'name', 'value': 'krn:modified_time'},
        {'prop': 'property', 'value': 'og:url'},
        {'prop': 'property', 'value': 'og:title'},
    ]

    def __init__(self, url):
        req = urllib.request.Request(url = url, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        })
        html = urllib.request.urlopen(req)
        self.soup = BeautifulSoup(html, 'html.parser')
        doc = self.extract_data()
        print(doc)        
    
    def build_datadoc(self, id, ressorts, published_time, modified_time, url, author, title, are_comments_allowed, tags, article_text):
        return {
            '_id': id,
            'title': title,
            'ressorts': ressorts,
            'published_time': published_time,
            'modified_time': modified_time,
            'url': url,
            'author': author,
            'are_comments_allowed': are_comments_allowed,
            'tags': tags,
            'article_text': article_text
        }

    def get_meta_content(self, meta_data):
        meta = self.soup.find('meta', { meta_data['prop']: meta_data['value']})
        if meta != None:
            return meta['content']
        return None

    def extract_data(self):       
        return self.build_datadoc(
            id = self.get_meta_content(self.meta_data[0]),   
            published_time = self.get_meta_content(self.meta_data[1]),
            modified_time = self.get_meta_content(self.meta_data[2]),
            url = self.get_meta_content(self.meta_data[3]),
            title=self.get_meta_content(self.meta_data[4]),
            ressorts = self.get_ressorts(),
            author = self.get_author(),
            are_comments_allowed=self.are_comments_allowed(),
            tags=self.get_tags(),
            article_text=self.get_article_text()
        )

    # ========= Implement in subclasses ==========

    def get_ressorts(self):
        pass

    def get_subressort(self, ressorts, ressorts_text):
       pass

    # Note: Some articles don't have an author
    def get_author(self):
        pass

    def are_comments_allowed(self):
        pass

    def get_tags(self):        
        pass
    
    def get_article_text(self):
        pass
