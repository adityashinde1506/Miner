import logging
import pandas


class RecordMiner:
    """
        Reads cap files from sysdig and extract relevant processes.
    """

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.store_dir = "../data/"

    def extract_relevant_records(self, pid, filename):
        # Read the pandas dataframe.
        dataframe = pandas.read_csv(filename,
                                    header=None,
                                    index_col=None)
        logging.debug(f"Read {dataframe.shape[0]} records")

        dataframe.columns = ["parent",
                             "parent_pid",
                             "process",
                             "pid",
                             "event",
                             "dir"]

        print(dataframe["pid"].unique())
        print(f"Looking for {pid}")
        print(dataframe.head(5))

        dataframe = dataframe[(dataframe["pid"] == pid) |
                              (dataframe["parent_pid"] == pid)]

        if dataframe.shape[0] > 0:
            logging.debug(f"{dataframe.shape[0]} records found to be relevant \
                           to {pid}")
            print(dataframe.head(10))

            # Write to file
            store_file = self.store_dir+f"{str(dataframe['pid'].unique()[0])}_{dataframe['process'].unique()[-1]}.csv"
            dataframe.to_csv(store_file)
            self.logger.debug(f"Log written to {store_file}")
