import bas.config as config
from bas.system_master import SystemMaster
from bas.dev.server import DevServer, server_input_queue


def run_game():
    print('Birds & Snakes\n')

    if config.is_dev_mode():
        server = DevServer()
        input_queue = server_input_queue

    system_master = SystemMaster(input_queue)

    try:
        if config.is_dev_mode():
            server.start()
        system_master.start()
    except SystemExit:
        system_master.stop()
        if config.is_dev_mode():
            server.stop()
    finally:
        system_master.join()
        print('-- game ended --')
