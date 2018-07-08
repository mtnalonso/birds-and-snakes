import logging
from bas.message import Message


logger = logging.getLogger(__name__)


class DevInterface:
    def __init__(self, queue=None):
        self.queue = queue

    def start(self):
        print('[DEV MODE]')
        self.__request_new_message()

    def __request_new_message(self):
        input_message = input('> ')
        self.__handle_if_command(input_message)
        try:
            self.__add_message_to_queue(input_message)
        except ValueError:
            print('ERROR!\nMessage format -> USER: MESSAGE')
            self.__request_new_message()

    def __handle_if_command(self, message):
        if message in ['exit', ':q']:
            raise SystemExit

    def __add_message_to_queue(self, message):
        message = Message.from_string(message)
        self.queue.put(message)

    def send_reply(self, response):
        print('\n-> {}\n'.format(response))
        self.__request_new_message()
