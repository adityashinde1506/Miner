import logging
import time
import argparse

logging.basicConfig(level=logging.DEBUG)


def get_cmdline():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', help="name of the output file.", action="store")
    parser.add_argument()
