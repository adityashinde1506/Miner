import logging


class LogHandler(object):
    """
        Parses audit logs for creating data.
    """

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.info("Log handler initialised.")

    def read_logs(self):
        with open("/var/log/audit/audit.log") as log_file:
            print(log_file.readline())
