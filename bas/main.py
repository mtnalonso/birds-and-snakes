from queue import Queue
from bas.game_master import GameMaster
from bas.dev_interface import DevInterface


def run_game(args):
    print('Birds & Snakes')
    input_queue = Queue()
    run_game_safe(input_queue, args)


def run_game_safe(input_queue, args):

    if args.dev:
        dev_interface = DevInterface(input_queue)
        game_master = GameMaster(input_queue, dev_interface)
    else:
        game_master = GameMaster(input_queue)

    try:
        game_master.start()
        if args.dev:
            dev_interface.start()
    except SystemExit:
        game_master.stop()
    finally:
        game_master.join()
        print('-- game ended --')
