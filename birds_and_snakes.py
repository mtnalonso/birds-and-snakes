import sys
import argparse
import logging
import logging.handlers
from logging.config import dictConfig

from bas.dev.client import DevClient
from bas.main import run_game
from bas.manager import Manager


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
    parser = argparse.ArgumentParser(prog='birds_and_snakes.py',
                                     epilog='Enjoy the game!')
    parser.add_argument('-c', '--client', action='store_true',
                        help='Launch debug client')
    parser.add_argument('-m', '--manager', metavar='COMMAND',
                        help='Manager interface')
    return parser.parse_args()


def handle_args():
    args = load_args()

    if args.client:
        run_client()
    if args.manager:
        Manager().command(args.manager)
        sys.exit()
    return


def run_client():
    client = DevClient()
    client.start()
    client.join()
    sys.exit()


if __name__ == '__main__':
    handle_args()
    run_game()
