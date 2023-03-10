import pytest
import os
import json
from dataclasses import dataclass
from unittest import mock
from app.utils import destination


@dataclass
class MockResponse:
    status_code: int
    example_html: str
    url: str = "http://thousandtrails.com/state/park"

    def response(self):
        resp = mock.Mock()
        resp.status_code = self.status_code
        resp.content = self.html()

        return resp

    def html(self):
        this_dir = os.path.dirname(__file__)
        return open(os.path.join(this_dir, self.example_html)).read()


class TestScraper:
    @mock.patch('requests.get')
    def test_state(self, mock_get):
        mock = MockResponse(200, '../examples/resort.html')
        mock_get.return_value = mock.response()
        resort = destination.parse(mock.url)

        assert resort.state() == "state"
        assert resort.title() == "Acorn Campground"
        assert "Acorn Campground is nestled in beautiful southern Cape May" in resort.description()
        assert sorted(resort.details().keys()) == sorted(['address', 'season', 'sites', 'membership'])
        assert sorted(resort.accomodations().keys()) == sorted(['rental accommodations', 'rv sites', 'tent sites'])
        assert 'swimming pool' in resort.available_amenities()


