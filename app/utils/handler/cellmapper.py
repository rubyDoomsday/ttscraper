class Cellmapper:
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

    def att(self):
        return f"https://www.cellmapper.net/map?MCC=310&MNC=410&type=LTE&latitude={self.lat}&longitude={self.lng}&zoom=13&showTowers=true"

    def verizon(self):
        return f"https://www.cellmapper.net/map?MCC=311&MNC=480&type=LTE&latitude={self.lat}&longitude={self.lng}&zoom=13&showTowers=true"

