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
    'att_bars',
    'verizon_bars',
    'encore',
    'att_link',
    'verizon_link',
]

def write(destination, resort, filename = 'results.csv'):
    CSV(destination, resort, filename).write()

class CSV:
    def __init__(self, destination, resort, filename):
        self.destination = destination
        self.resort = resort
        self.filename = filename

    def write(self):
        f = open(self.filename, 'w')
        writer = csv.writer(f)
        resorts = self.resort.all()
        writer.writerow(headers)
        for r in resorts:
            resort_ = self.destination.parse(r)
            print(resort_.url)
            try:
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
                    resort_.signal()['att'],
                    resort_.signal()['verizon'],
                    resort_.encore(),
                    resort_.cellMapper().att(),
                    resort_.cellMapper().verizon(),
                ]
                writer.writerow(row)
            except Exception as e:
                print("failure", e)
                continue

        f.close()

