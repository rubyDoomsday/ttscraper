import csv
from utils import resort, scraper

# url = 'https://www.thousandtrails.com/new-jersey/acorn-campground'
# print(json.dumps(resort(url), indent=4))

def show():
    resorts = resort.all()
    for r in resorts : print(scraper.parse(r).to_json())

def write():
    f = open('results.csv', 'w')
    writer = csv.writer(f)
    resorts = resort.all()
    header = [
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
    ]
    writer.writerow(header)
    for r in resorts:
        _resort = scraper.parse(r)
        print(_resort.url)
        row = [
            _resort.state(),
            _resort.title(),
            _resort.url,
            _resort.accomodations()['rv sites'],
            _resort.accomodations()['rental accommodations'],
            _resort.amenities()['fitness center'],
            _resort.amenities()['laundry facilities'],
            _resort.amenities()['pickleball'],
            _resort.amenities()['private mailbox/mail center'],
            _resort.amenities()['restroom/shower facilities'],
            _resort.amenities()['rv storage'],
            _resort.amenities()['swimming pool'],
            _resort.amenities()['tennis courts'],
            _resort.amenities()['whirlpool/spa/hot tub'],
            _resort.available_amenities(),
            _resort.maplink(),
            _resort.description(),
            _resort.details()['address'],
            _resort.details()['open/close'],
        ]
        writer.writerow(row)

    f.close()

def main():
    write()
    # show()

if __name__=='__main__':
    main()
