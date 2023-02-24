import csv

headers = [
    'state',
    'title',
    'reserve',
    'rv sites',
    'rentals',
    'fitness center',
    'laundry',
    'pickleball',
    'mail',
    'shower',
    'rv storage',
    'pool',
    'tennis courts',
    'hot tub',
    'all amenities',
    'map',
    'description',
    'address',
    'season',
    'latitude',
    'longitude',
    'encore',
]

def write(scraper, resort, filename = 'results.csv'):
    CSV(scraper, resort, filename).write()

class CSV:
    def __init__(self, scraper, resort, filename):
        self.scraper = scraper
        self.resort = resort
        self.filename = filename

    def write(self):
        f = open(self.filename, 'w')
        writer = csv.writer(f)
        resorts = self.resort.all()
        writer.writerow(headers)
        for r in resorts:
            resort_ = self.scraper.parse(r)
            print(resort_.url)
            row = [
                resort_.state(),
                resort_.title(),
                resort_.url,
                resort_.accomodations()['rv sites'],
                resort_.accomodations()['rental accommodations'],
                resort_.amenities()['fitness center'],
                resort_.amenities()['laundry facilities'],
                resort_.amenities()['pickleball'],
                resort_.amenities()['private mailbox/mail center'],
                resort_.amenities()['restroom/shower facilities'],
                resort_.amenities()['rv storage'],
                resort_.amenities()['swimming pool'],
                resort_.amenities()['tennis courts'],
                resort_.amenities()['whirlpool/spa/hot tub'],
                resort_.available_amenities(),
                resort_.maplink(),
                resort_.description(),
                resort_.details()['address'],
                resort_.details()['season'],
                resort_.gps()['latitude'],
                resort_.gps()['longitude'],
                resort_.encore()
            ]
            writer.writerow(row)

        f.close()

