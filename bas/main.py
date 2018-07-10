from queue import Queue
from bas.game_master import GameMaster
from bas.dev.server import DevServer, server_input_queue


def run_game(args):
    print('Birds & Snakes')

    if args.dev:
        server = DevServer()
        input_queue = server_input_queue

    game_master = GameMaster(input_queue)

    try:
        if args.dev:
            server.start()
        game_master.start()
    except SystemExit:
        game_master.stop()
        if args.dev:
            server.stop()
    finally:
        game_master.join()
        print('-- game ended --')
