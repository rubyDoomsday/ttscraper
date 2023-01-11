import requests
import json
from bs4 import BeautifulSoup

ACCOMODATIONS = [
    "explore rv sites",
    "explore rental accommodations",
    "explore tent sites"
]

AMENITIES = [
    "fitness center",
    "laundry facilities",
    "pickleball",
    "private mailbox/mail center",
    "restroom/shower facilities",
    "rv storage",
    "swimming pool",
    "tennis courts",
    "whirlpool/spa/hot tub",
]

class Scraper:
    def __init__(self, url):
        resp = requests.get(url)
        self.url = url
        self.page = BeautifulSoup(resp.content, 'html.parser')

    def to_json(self):
        return json.dumps({
            'state': self.state(),
            'title': self.title(),
            'url': self.url,
            'details':  self.details(),
            'description': self.description(),
            'accomodations': self.accomodations(),
            'available_amenities': self.available_amenities(),
            'amenities': self.amenities(),
            'resort_map': self.maplink(),
        }, indent=4)

    def state(self):
        return self.url.split('/')[3]

    def title(self):
        return self.page.title.text

    def overview(self):
        return self.page.find('section', id='resort-overview')

    def description(self):
        description = self.overview().find('p', class_='resort-description')
        return description.text

    def details(self):
        meta = self.overview().find('div', class_='resort-meta')
        _details = meta.find_all('div', class_="meta-item")
        details = {}
        for detail in _details:
            try:
              key, value = detail.text.split(':')
              details[key.strip().lower()] = value.strip().lower()
            except:
              key = detail.text
              details[key.strip().lower()] = "true"

        return details

    def accomodations(self):
        article = self.page.find('article', id='resort-sites')
        spans = list(map(lambda x: x.text.lower(), article.find_all('span')))
        accomodations = {}
        for a in ACCOMODATIONS:
            if a in spans:
                accomodations[a.replace("explore", "").strip()] = "true"
            else:
                accomodations[a.replace("explore", "").strip()] = "false"

        return accomodations

    def available_amenities(self):
        section = self.page.find('ul', class_='amenities-list')
        return list(map(lambda x: x.text.lower(), section.find_all('li')))

    def amenities(self):
        amenities = {}
        for feature in AMENITIES:
            if feature in self.available_amenities():
              amenities[feature] = 'true'
            else:
              amenities[feature] = 'false'

        return amenities

    def maplink(self):
        location = self.page.find('section', id='resort-location')
        mapLink = location.find_all('a')
        mapLink.reverse()
        url = mapLink[0].get('href')
        return url

def parse(url):
    return Scraper(url)
