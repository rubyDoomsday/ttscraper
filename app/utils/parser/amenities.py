import json

AmenitiesClass = 'amenities-list'

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

def new(page):
    return Amenities(page)

class Amenities:
    def __init__(self, page):
        self.page = page
        self.results = {}

        self.__build()

        self.to_json = json.dumps(self.results, indent=4)
        self.labels = self.results.keys()

    def __build(self):
        for feature in AMENITIES:
            if feature in self.all():
              self.results[feature] = 'true'
            else:
              self.results[feature] = 'false'

    def all(self):
        return list(map(lambda x: x.text.lower(), self.__section().find_all('li')))

    def __section(self):
        return self.page.find('ul', class_=AmenitiesClass)
