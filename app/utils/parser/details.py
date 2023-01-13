import json

OverviewID = 'resort-overview'
SectionTag = 'resort-meta'
ItemTag = 'meta-item'
true_ = 'true'

DetailMap = {
    'address': 'address',
    'number of sites': 'sites',
    'open/close': 'season',
    'membership': 'membership',
    'age qualified': 'age qualified',
}
def new(page):
    return Details(page)

class Details:
    def __init__(self, page):
        self.page = page
        self.results = {}

        self.__build()

        self.to_json = json.dumps(self.results, indent=4)
        self.labels = self.results.keys()

    def __build(self):
        for detail in self.__detail_list():
            try:
                label, value = detail.text.split(':')
                self.results[DetailMap[label.strip().lower()]] = value.strip().lower()
            except:
                label = detail.text
                self.results[DetailMap[label.strip().lower()]] = 'true'

    def __detail_list(self):
        return self.__section().find_all('div', class_=ItemTag)

    def __section(self):
        return self.__overview().find('div', class_=SectionTag)

    def __overview(self):
        return self.page.find('section', id=OverviewID)

