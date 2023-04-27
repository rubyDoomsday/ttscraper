import pytest
import os
import json
from dataclasses import dataclass
from unittest import mock
from app.utils import campendium


@dataclass
class MockResponse:
    status_code: int
    example_html: str
    url: str = "https://www.campendium.com/moody-beach-thousand-trails"

    def response(self):
        resp = mock.Mock()
        resp.status_code = self.status_code
        resp.content = self.html()

        return resp

    def html(self):
        this_dir = os.path.dirname(__file__)
        return open(os.path.join(this_dir, self.example_html)).read()

class TestCampendiuum:
    def test_search_success(self):
        name = "Moody Beach Thousand Trails"
        cmpdm = campendium.Campendium(name)
        assert cmpdm.search() != None

    def test_search_failure(self):
        name = "Mt Desert Narrows Campground"
        cmpdm = campendium.Campendium(name)
        assert cmpdm.search() == None

class TestCampendiuumScraper:
    @mock.patch('requests.get')
    def test_scraper(self, mock_get):
        mock = MockResponse(200, '../examples/campendiuum-result.html')
        mock_get.return_value = mock.response()
        campground = campendium.CellSignal(mock.url)

        signal = campground.signal()
        assert len(signal) == 3
        assert signal['verizon'] == 3
        assert signal['att'] == 3
        assert signal['tmobile'] == 3
