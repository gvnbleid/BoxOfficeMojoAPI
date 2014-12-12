#!/usr/bin/python

"""
Box Office Mojo API
Unofficial Python API for Box Office Mojo API.

Author: Justin Cano
Email: jcano001@ucr.edu
License: MIT
"""
import urllib
import urllib2
import unittest
import vcr

from bs4 import BeautifulSoup
from bom import BOM, BASE_URL, WEEKEND_CHART
from test_utils import FIXTURES_DIR


class TestBOM(unittest.TestCase):

    @vcr.use_cassette(FIXTURES_DIR + '/vcr_cassettes/bom.yaml')
    def setUp(self):
        self.bom = BOM()
        movies = self.bom.get_movies()
        self.test_movie = movies.next() # get the first movie for testing

    def test_bom(self):
        """
        Tests if BOM holds appropriate Movie objects
        """
        assert type(self.test_movie.rank) == int
        assert type(self.test_movie.title) == str
        assert type(self.test_movie.studio) == str
        assert type(self.test_movie.gross_str) == str
        assert "$" in self.test_movie.gross_str
        assert type(self.test_movie.gross_int) == int

    @vcr.use_cassette(FIXTURES_DIR + '/vcr_cassettes/weekend_trend.yaml')
    def test_weekend_trend(self):
        """
        Tests for the weekend trend of a movie
        """
        trend_data = self.test_movie.weekend_trend()
        assert type(trend_data) == list
        print trend_data
        for data in trend_data:
            assert type(data) == tuple





if __name__ == '__main__':
    unittest.main()
