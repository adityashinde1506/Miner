import unittest
import sys
import logging


sys.path.append("/home/adityas/Projects/LogAnalyser/")
logging.basicConfig(level=logging.DEBUG)

from loganalyser.data_recorder.data_recorder import Recorder


class TestRecorder(unittest.TestCase):

    def setUp(self):
        self.recorder = Recorder()

    def test_recorder_init(self):
        print(self.recorder)
