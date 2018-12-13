import subprocess
import logging
import time
import random
import signal
import os
from loganalyser.activitygenerator.base_activity import BaseActivity


class OpenFileActivity(BaseActivity):

    def __init__(self, test_file="/home/adityas/.bashrc"):
        # List of text editors which can open files
        self.open_apps = ["leafpad"]

        self.filename = test_file

        self.logger = logging.getLogger(self.__class__.__name__)

    def perform_activity(self):
        app = random.choice(seq=self.open_apps)
        self.logger.info(f"Running command {app} {self.filename}")
        self.proc = subprocess.Popen([app, self.filename], shell=True)

    def repeat_perform_activity(self, wait_time, iterations):
        for i in range(iterations):
            self.perform_activity()
            time.sleep(wait_time)
            self.stop_activity()
            time.sleep(1)

    def stop_activity(self):
        self.proc.terminate()
        # os.killpg(os.getpgid(self.proc.pid), signal.SIGTERM)
