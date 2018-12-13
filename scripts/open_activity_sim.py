import sys
import logging
import argparse
import time


logging.basicConfig(level=logging.DEBUG)
sys.path.append("/home/adityas/Projects/LogAnalyser")


from loganalyser.data_recorder.data_recorder import Recorder
from loganalyser.activitygenerator.open_file_activity import OpenFileActivity
from loganalyser.activitygenerator.navigation_activity import FixedNavigationActivity
from loganalyser.data_recorder.record_miner import RecordMiner


def parse_cmdline():
    parser = argparse.ArgumentParser()
    parser.add_argument("i", help="number of iterations")
    parser.add_argument("f", help="filename to store")
    return parser.parse_args()


def main():

    # Parse command line
    args = parse_cmdline()

    # initialise recorder and activity objects
    recorder = Recorder()
    activity = OpenFileActivity()
    miner = RecordMiner()

    # run simulation
    logging.info(f"Starting simulation for {args.i} iterations in {args.f}")

    for i in range(int(args.i)):
        recorder.start_recording(args.f)
        time.sleep(2)
        activity.repeat_perform_activity(wait_time=2, iterations=1)
        time.sleep(2)
        recorder.stop_recording()
        miner.extract_relevant_records(pid=activity.proc.pid,
                                       filename=args.f)

    logging.info(f"Finished sim. Data stored in {args.f}")


if __name__ == "__main__":
    main()
