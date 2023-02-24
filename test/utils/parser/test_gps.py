import pytest
import os
from bs4 import BeautifulSoup
from app.utils.parser import gps

class TestGps:
    def test_location_found(self):
        _obj = gps.new("6649 e. 32nd st., yuma, az")
        assert len(_obj.labels) == 2
        assert 'latitude' in _obj.labels
        assert 'longitude' in _obj.labels

    def test_location_not_found(self):
        _obj = gps.new("419 NJ-47, Villas, NJ 08251")
        assert len(_obj.labels) == 2
        assert 'latitude' in _obj.labels
        assert 'longitude' in _obj.labels
