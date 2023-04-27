import requests
import json
from bs4 import BeautifulSoup

PROVIDERS = {
  'Verizon 4G/5G': 'verizon',
  'Verizon 4G': 'verizon',
  'Verizon 5G': 'verizon',
  'AT&T 4G': 'att',
  'AT&T 5G': 'att',
  'AT&T 4G/5G': 'att',
  'T-Mobile 4G': 'tmobile',
  'T-Mobile 4G/5G': 'tmobile',
  'T-Mobile 5G': 'tmobile',
}

DEFAULT_SIGNALS = {
    'verizon': 0,
    'att': 0,
    'tmobile': 0,
}

def parse(campground_name):
    url = Campendium(campground_name).search()
    if url != None:
      return CellSignal(url).signal()
    else:
        return DEFAULT_SIGNALS

class Campendium:
    def __init__(self, name):
        self.name = name

    def search(self):
        resp = requests.get(self.search_url())
        if resp.url.find(self.search_url().split("?")[-1]) >= 1:
            return None
        else:
            return resp.url

    def search_url(self):
        query = "+".join(self.name.split(" "))
        return f"https://www.campendium.com/campgrounds/map?q={query}"

class CellSignal:
    def __init__(self, url):
        resp = requests.get(url)
        self.page = BeautifulSoup(resp.content, 'html.parser')

    def to_json(self):
        return json.dumps({
            'signal': self.signal(),
        }, indent=4)

    def signal(self):
        section = self.page.find('div', id='cell-signal')
        ratings = DEFAULT_SIGNALS

        if section == None:
            return ratings

        spans = section.find_all('span')
        labels = spans[1::2]
        imgs = spans[0::2]

        for i in range(len(labels)):
            text = labels[i].text
            src = imgs[i].img['src']
            ratings[PROVIDERS[text]] = self.__get_bars(src)

        return ratings

    def __get_bars(self, src):
        # pulls #bars text our of source svg
        xbars = src.split('/')[-1].split('-')[0]
        # grabs # from bar string
        return int(xbars.split('b')[0])
