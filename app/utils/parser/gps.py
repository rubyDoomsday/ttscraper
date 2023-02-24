import json
from dataclasses import dataclass
from geopy.geocoders import Nominatim

def new(address):
    return Gps(address)

class Gps:
    def __init__(self, address):
        self.address = address
        self.results = {}

        self.__build()

        self.to_json = json.dumps(self.results, indent=4)
        self.labels = self.results.keys()

    def __build(self):
        geolocator = Nominatim(user_agent="gps")
        try:
          location = geolocator.geocode(self.address)
        except Exception:
          location = emptyLocal()

        if location is None:
          location = emptyLocal()

        self.results = {
            "latitude": location.latitude,
            "longitude": location.longitude
        }

@dataclass
class emptyLocal():
    latitude: str = None
    longitude: str = None

