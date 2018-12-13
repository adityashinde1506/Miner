import os
import logging
from pathlib import Path


logging.basicConfig(level=logging.DEBUG)


def get_children(node):
    logging.info(f"Running ls on {node}")
    return list(node.iterdir())


def main():
    curr_dir = Path(os.getcwd())/"sim_dir"
    print(get_children(curr_dir))


if __name__ == "__main__":
    main()
