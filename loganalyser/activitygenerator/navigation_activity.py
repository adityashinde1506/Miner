import subprocess
import logging
import time
import random
import os
from loganalyser.activitygenerator.base_activity import BaseActivity


class FixedNavigationActivity(BaseActivity):

    def __init__(self, nav_script):
        self.nav_script = nav_script
        self.logger = logging.getLogger(self.__class__.__name__)

    def perform_activity(self):
        self.logger.info(f"Running command {self.nav_script}")
        self.proc = subprocess.Popen(self.nav_script)

    def repeat_perform_activity(self, wait_time, iterations):
        for i in range(iterations):
            self.perform_activity()
            time.sleep(10)
            self.stop_activity()
            time.sleep(1)

    def stop_activity(self):
        self.proc.wait()
        self.proc.kill()
        pass
