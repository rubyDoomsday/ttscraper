from .utils import scraper, resort, csv

def show(park):
    resorts = resort.all()
    if park == None:
        for r in resorts : print(scraper.parse(r).to_json())
    else:
        print(scraper.parse(resorts[int(park)]).to_json())

def run(opts):
    if opts.write == None:
        show(opts.park)
    else:
        csv.write(scraper, resort, opts.write)
