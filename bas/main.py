from queue import Queue

import bas.config as config
from bas.game_master import GameMaster
from bas.dev.server import DevServer, server_input_queue


def run_game():
    print('Birds & Snakes\n')

    if config.is_dev_mode():
        server = DevServer()
        input_queue = server_input_queue

    game_master = GameMaster(input_queue)

    try:
        if config.is_dev_mode():
            server.start()
        game_master.start()
    except SystemExit:
        game_master.stop()
        if config.is_dev_mode():
            server.stop()
    finally:
        game_master.join()
        print('-- game ended --')
