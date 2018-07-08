import argparse
import logging
import logging.handlers
from logging.config import dictConfig

from bas.main import run_game


logger = logging.getLogger(__name__)


def init_logger(debug):
    dictConfig(DEFAULT_LOGGING)
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)-8s %(name)-12s: %(message)s')
    logging.root.setLevel(logging.DEBUG)

    if debug:
        activate_stream_logging(formatter)
    activate_file_logging(formatter)


def activate_stream_logging(formatter):
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logging.root.addHandler(console_handler)


def activate_file_logging(formatter):
    file_handler = logging.FileHandler(
        'history.log',
        mode='w',
        encoding='utf-8'
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    logging.root.addHandler(file_handler)


def load_args():
    parser = argparse.ArgumentParser(prog='birds_and_snakes.py')
    parser.add_argument('-d', '--dev', action='store_true',
                        help='Use development interface')
    return parser.parse_args()


if __name__ == '__main__':
    args = load_args()
    run_game(args)
