import pytest
import os
import json
from dataclasses import dataclass
from unittest import mock
from app.utils import resort


@dataclass
class MockResponse:
    status_code: int
    example_html: str
    url: str = 'https://newbook.thousandtrails.com/'

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
        mock = MockResponse(200, '../examples/index.html')
        mock_get.return_value = mock.response()
        resort_urls = resort.all()

        assert len(resort_urls) == 223



