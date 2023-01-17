import pytest
import os
from bs4 import BeautifulSoup
from app.utils.parser import accommodations

@pytest.fixture
def mock_page():
    this_dir = os.path.dirname(__file__)
    return BeautifulSoup(
                open(os.path.join(this_dir, '../../examples/resort.html')),
                "html.parser"
           )

def test_labels(mock_page):
    _obj = accommodations.new(mock_page)
    assert len(_obj.labels) == 3
    assert 'rv sites' in _obj.labels
    assert 'rental accommodations' in _obj.labels
    assert 'tent sites' in _obj.labels

def test_to_json(mock_page):
    _obj = accommodations.new(mock_page)
    assert _obj.to_json == '{\n    "rv sites": "true",\n    "rental accommodations": "false",\n    "tent sites": "false"\n}'

def test_results(mock_page):
    _obj = accommodations.new(mock_page)
    assert _obj.results['rv sites'] == "true"
    assert _obj.results['rental accommodations'] == "false"
    assert _obj.results['tent sites'] == "false"
