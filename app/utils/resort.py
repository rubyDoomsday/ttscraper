import requests
import json
from bs4 import BeautifulSoup

INVALID_SITES = [
    "hiawassee-koa",
    "timber-creek-rv-resort",
]

class Resort:
    @classmethod
    def print(cls):
        for resort in Resort.all():
            print(resort)

    @classmethod
    def all(cls):
      return Resort('https://newbook.thousandtrails.com/').load()

    def __init__(self, url):
        self.url = url

    def load(self):
        page = self.__load_page()
        right_panel = page.find('div', id='newbook_crs_result_elements')
        links = right_panel.find_all('a')
        resorts = list(map(lambda x:x.get('href'), links))
        return self.__clean(resorts)

    def __load_page(self):
        resp = requests.get(self.url)
        print(resp)
        return  BeautifulSoup(resp.content, 'html.parser')

    def __clean(self, lst):
        for invalid in INVALID_SITES:
            for url in lst:
                if invalid in url:
                  lst.remove(url)

        return lst

def all():
    return Resort.all()

# -- Debugging
# print(Resort.print())


