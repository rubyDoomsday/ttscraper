import pytest
import os
from dataclasses import dataclass
from unittest import mock
from app.utils import scraper

@dataclass
class MockResponse:
    response: int

    def html(self):
        this_dir = os.path.dirname(__file__)
        return open(os.path.join(this_dir, '../examples/resort.html'))

mock_url = "http://thousandtrails.com/state/park"

@mock.patch('requests.get')
def test_state(mock_url, mock_get):
    mock_get.return_value = MockResponse(200)
    resort = scraper.parse(mock_url)

# def test_to_json(mock_url):
#     resort = scraper.parse(mock_url)
#
# def test_title(mock_url):
#     resort = scraper.parse(mock_url)
#
# def test_overview(mock_url):
#     resort = scraper.parse(mock_url)
#
# def test_details(mock_url):
#     resort = scraper.parse(mock_url)
#
# def test_accommodations(mock_url):
#     resort = scraper.parse(mock_url)
#
# def test_amenities(mock_url):
#     resort = scraper.parse(mock_url)
#
# def test_maplink(mock_url):
#     resort = scraper.parse(mock_url)
