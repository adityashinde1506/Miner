import logging
import subprocess
import argparse
import time


class Recorder(object):
    """
        Recorder class starts and stops sysdig.
    """

    def __init__(self, command=None):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.__command = 'sysdig -p %evt.time,%proc.name,%proc.pid,%proc.pname,%proc.ppid,%evt.type'
        self.sysdig = None
        self.logger.info("Initialised data recorder.")
        self.logger.debug(f"Data recorder command: {self.__command}")

# def get_cmdline():
#     """
#         Parse command line arguments and return values for output file and
#         file size.
#     """
#     parser = argparse.ArgumentParser()
#     parser.add_argument("w", help="name of the output file.")
#     parser.add_argument("t", help="time to run sysdig.")
#     args = parser.parse_args()
#     logging.info(f"Starting data gathering.")
#     return args
#
#
# def gather_data(output_file, run_time):
#     """
#         Start sysdig data capture.
#     """
#     logging.info(f"Starting to gather data in {output_file} for {run_time}sec")
#     command = f'sysdig -p %evt.time,%proc.name,%proc.pid,%proc.pname,%proc.ppid,%evt.type'
#     logging.debug(f"Running command: {command}")
#     with open(output_file, 'w') as o_file:
#         sysdig = subprocess.Popen(command.split(), stdout=o_file)
#         time.sleep(int(run_time))
#         sysdig.terminate()
#     logging.info(f"Finished recording data. Closing {sysdig}")
