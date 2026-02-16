import requests
from bs4 import BeautifulSoup


def extract():
    headers = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'
    URL = "https://realpython.github.io/fake-jobs/"
    page = requests.get(URL, headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_ = 'card')
    for item in divs:
        title = item.find(class_ = 'title').text
        print (title)
    return 

c = extract()
transform(c)
