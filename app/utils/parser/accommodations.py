import json

ResortID = 'resort-sites'

ACCOMODATIONS = [
    "explore rv sites",
    "explore rental accommodations",
    "explore tent sites"
]

def new(page):
    return Accommodations(page)

class Accommodations:
    def __init__(self, page):
        self.page = page
        self.results = {}

        self.__build()

        self.to_json = json.dumps(self.results, indent=4)
        self.labels = self.results.keys()

    def __build(self):
        for val in ACCOMODATIONS:
            if val in self.__spans():
                self.results[val.replace("explore", "").strip()] = "true"
            else:
                self.results[val.replace("explore", "").strip()] = "false"

    def __detail_list(self):
        return self.__section().find_all('div', class_=ItemTag)

    def __spans(self):
        return list(map(lambda x: x.text.lower(), self.__section().find_all('span')))

    def __section(self):
        return self.page.find('article', id=ResortID)


