import logging
import unittest
import sys

sys.path.append("/home/adityas/Projects/LogAnalyser")

from loganalyser.loghandler import LogHandler


class TestHandler(unittest.TestCase):

    def setUp(self):
        self.handler = LogHandler()

    def test_
