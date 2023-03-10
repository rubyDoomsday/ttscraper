from .utils import destination, resort, csv

def run(args):
    Ttscraper(args).run()

class Ttscraper:
    def __init__(self, args):
        self.args = args

    def run(self):
        if self.args.write == None:
            self.__show(self.args.park)
        else:
            csv.write(destination, resort, self.args.write)

    def __show(self, park):
        resorts = resort.all()
        if park == None:
            for r in resorts : print(destination.parse(r).to_json())
        else:
            print(destination.parse(resorts[int(park)]).to_json())
