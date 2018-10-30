import logging
import subprocess


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

    def start_recording(self, log_file):
        """
            Starts sysdig and outputs the logs to the given file
        """
        self.__l_file = open(log_file, 'w')
        self.sysdig = subprocess.Popen(self.__command.split(),
                                       stdout=self.__l_file)
        self.logger.info(f"Data recording started. Logging in {log_file}")

    def stop_recording(self):
        """
            Terminates sysdig process.
        """
        self.__l_file.close()
        self.sysdig.terminate()
        self.logger.info(f"Data recording stopped.")
