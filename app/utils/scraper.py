import requests
import json
from bs4 import BeautifulSoup
from .parser import details, accommodations, amenities, gps

def parse(url):
    return Scraper(url)

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
            'gps': self.gps(),
            'encore': self.encore(),
        }, indent=4)

    def encore(self):
        if 'encore' in self.title().lower():
            return 'true'
        else:
            return 'false'

    def gps(self):
        return gps.new(self.details()['address']).results

    def state(self):
        return self.url.split('/')[3]

    def title(self):
        return self.page.title.text.split('|')[0].strip()

    def description(self):
        description = self.__overview().find('p', class_='resort-description')
        return description.text

    def details(self):
        return details.new(self.page).results

    def accomodations(self):
        return accommodations.new(self.page).results

    def available_amenities(self):
        return amenities.new(self.page).all()

    def amenities(self):
        return amenities.new(self.page).results

    def maplink(self):
        location = self.page.find('section', id='resort-location')
        mapLink = location.find_all('a')
        mapLink.reverse()
        url = mapLink[0].get('href')
        return url

    def __overview(self):
        return self.page.find('section', id='resort-overview')

