import requests
from bs4 import BeautifulSoup

head = {
    "User-Agent":"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52"
}

def get_content(url):
    targets = []
    html = requests.get(url, headers=head)
    print(html.status_code)
    content = html.content
    soup = BeautifulSoup(content,"lxml")
    for link in soup.findAll("a"):
        ref = link.get("href")
        if ref.startswith('http') == False:
            if ref not in targets and ref.startswith('/'):
                targets.append(ref)
    c = 1
    for l in targets:
        print("Element: {} - > {}".format(c,l))
        c +=1
    print(soup.prettify())


get_content("https://www.kali.org/")