import os
import json
from dotenv import load_dotenv
import requests

def new(address):
    load_dotenv()
    token = os.getenv('MAPS_API_KEY')
    return Coordinates(token, address)

class Coordinates:
    def __init__(self, token, address):
        self.token = token
        self.address = address
        self.results = {}

        self.__build(address)

        self.to_json = json.dumps(self.results, indent=4)

    def __build(self, address):
        resp = requests.get(self.__url(), params=self.__payload(address)).json()
        location = resp['results'][0]['geometry']['location']

        self.results = {
            "latitude": location['lat'],
            "longitude": location['lng']
        }

    def __url(self):
        return 'https://maps.googleapis.com/maps/api/geocode/json'

    def __payload(self,address):
        return {
            'address': address,
            'key': self.token
        }
