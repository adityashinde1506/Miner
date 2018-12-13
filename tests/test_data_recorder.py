import unittest
import sys
import logging
import time
import pathlib


sys.path.append("/home/adityas/Projects/LogAnalyser/")
logging.basicConfig(level=logging.DEBUG)

from loganalyser.data_recorder.data_recorder import Recorder


class TestRecorder(unittest.TestCase):

    def setUp(self):
        self.recorder = Recorder()
        self.test_file = "../data/test.cap"

    def test_recorder_init(self):
        print(self.recorder)

    def test_recorder_switching(self):
        self.recorder.start_recording(log_file=self.test_file)
        print("Testing logging wait for 5 secs.")
        time.sleep(5)
        self.recorder.stop_recording()
        self.assertTrue(pathlib.Path(self.test_file).exists())

    def tearDown(self):
        print("Removing test file")
        _file = pathlib.Path(self.test_file)
        _file.unlink()
        print(f"File exists: {_file.exists()}")
