import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

class Request:

    # Constructor of Request
    def __init__(self, url, head):
        self.url = url
        self.header = head
        self.content = None
        self.status_code = None
        self.reason = ''

    # Function that obtains html code from url - Request
    def get_content(self):
        try:
            target = check_url(self.url)
            req = requests.get(target, headers=self.header, timeout=1)
            self.status_code = req.status_code
            self.reason = req.reason
            if req.status_code == 200:
                html = req.content
                soup = BeautifulSoup(html,'lxml')
                self.content = soup
        except Exception:
            print('[ERROR] Domain not found --> {}'.format(target))

    # Function that obtains links to pages to be scanned
    def get_links_hrefs(self):
        links = list()
        if self.content != None:
            elements = self.content.findAll('a')
            for a in elements:
                href = a.get('href')
                links.append(href)
        return links

    # Function that obtains links to img to be downloaded
    def get_links_img(self):
        links = list()
        if self.content != None:
            elements = self.content.findAll('img')
            for img in elements:
                src = img.get('src')
                links.append(src)
        return links


# Function that checks the syntax 'http' of a url [origin]
def check_url(origin):
    parser = urlparse(origin)
    if parser.scheme == '':
        url = 'http://'+parser.path
        return url
    else:
        return origin
