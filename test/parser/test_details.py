import pytest
import os
from bs4 import BeautifulSoup
from app.utils.parser import details

@pytest.fixture
def mock_page():
    this_dir = os.path.dirname(__file__)
    return BeautifulSoup(
                open(os.path.join(this_dir, '../examples/resort.html')),
                "html.parser"
           )

def test_detail_labels(mock_page):
    _obj = details.new(mock_page)
    assert len(_obj.labels) == 4
    assert 'address' in _obj.labels
    assert 'sites' in _obj.labels
    assert 'season' in _obj.labels
    assert 'membership' in _obj.labels

def test_details_to_json(mock_page):
    _obj = details.new(mock_page)
    assert _obj.to_json == '{\n    "address": "419 route 47 south, green creek, nj",\n    "season": "05/07/2023 \\u2014 09/25/2023",\n    "sites": "318",\n    "membership": "trails collection"\n}'

def test_details_results(mock_page):
    _obj = details.new(mock_page)
    assert _obj.results['address'] == "419 route 47 south, green creek, nj"
    assert _obj.results['season'] == "05/07/2023 — 09/25/2023"
    assert _obj.results['sites'] == "318"
    assert _obj.results['membership'] == "trails collection"
