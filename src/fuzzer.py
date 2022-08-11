import requests
from bs4 import BeautifulSoup
from os.path import abspath
from os import getcwd

default_level = 5
default_head = {"User-Agent":"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52"}
default_path = abspath(getcwd())+"/data"

class Fuzzer:

    def __init__(self, url, path=default_path):
        self.url = url
        self.level = 0
        self.path = path
        self.targets = []
    
    def get_content(self):
        req = requests.get(self.url, headers=default_head)
        if req.status_code == 200:
            content = req.content
            soup = BeautifulSoup(content,"lxml")
            return soup
        else:
            print("Error fuzzing --> {}".format(self.url))
            print("Status code: {}".format(req.status_code))
            return None

    def get_hrefs(self):
        soup = self.get_content()
        if soup != None:
            hrefs = soup.findAll('a')
            for link in hrefs:
                content = link.get('href')
                if content.startswith(self.url) or content.startswith("/"):
                    if content not in self.targets:
                        self.targets.append(content)   
    
    def print_result(self):
        self.targets.sort()
        for link in self.targets:
            print(link)

    def print_fuzzer(self):
        pass