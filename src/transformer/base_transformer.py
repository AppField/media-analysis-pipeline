from bs4 import BeautifulSoup
import urllib.request


class Transformer():
    # change prop and value attributes in subclasses
    meta_data = [
        {'prop': 'name', 'value': 'krn:published_time'},
        {'prop': 'name', 'value': 'krn:modified_time'},
        {'prop': 'property', 'value': 'og:url'},
        {'prop': 'property', 'value': 'og:title'},
    ]

    def __init__(self, html):
        self.soup = BeautifulSoup(html, 'html.parser')        

    def build_datadoc(self, id, ressorts, published_time, modified_time, url, author, title, are_comments_allowed, tags, article_text, is_plus):
        return {
            'title': title,
            'ressorts': ressorts,
            'published_time': published_time,
            'modified_time': modified_time,
            'url': url,
            'author': author,
            'are_comments_allowed': are_comments_allowed,
            'tags': tags,
            'article_text': article_text,
            'is_plus': is_plus
        }

    def get_meta_content(self, meta_data):
        meta = self.soup.find('meta', {meta_data['prop']: meta_data['value']})
        if meta != None:
            return meta['content']
        return None

    def extract_data(self):
        return self.build_datadoc(
            id=self.get_article_id(),
            published_time=self.get_meta_content(self.meta_data[0]),
            modified_time=self.get_meta_content(self.meta_data[1]),
            url=self.get_meta_content(self.meta_data[2]),
            title=self.get_meta_content(self.meta_data[3]),
            ressorts=self.get_ressorts(),
            author=self.get_author(),
            are_comments_allowed=self.are_comments_allowed(),
            tags=self.get_tags(),
            article_text=self.get_article_text(),
            is_plus=self.is_plus()
        )

    # ========= Implement in subclasses ==========

    def get_article_id(self):
        pass

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

    def is_plus(self):
        pass
