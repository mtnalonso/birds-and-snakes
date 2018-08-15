from datetime import datetime
from threading import Thread
from queue import Queue
from uuid import uuid4

from bas.nlp.message_handler import MessageHandler


class GameMaster(Thread):
    def __init__(self, system_master):
        Thread.__init__(self)
        self.__id = uuid4().hex
        self.system_master = system_master
        self.queue = Queue()
        self.message_handler = MessageHandler(self)
        self.game = None
        print('[+] Started Game Master #{}'.format(self.__id))

    @property
    def id(self):
        return self.__id

    def start(self):
        self.is_running = True
        super().start()

    def run(self):
        while self.is_running:
            self.update()
        return

    def update(self):
        if not self.queue.empty():
            self.process_message()
        return

    def stop(self):
        self.is_running = False

    def new_message(self, message):
        self.queue.put(message)

    def process_message(self):
        message = self.queue.get()
        print('\n{}\n'.format(message))
        response_message = self.message_handler.process(message)
        print(response_message + '\n') 

    def add_user(self, user):
        self.system_master.add_user(self, user)
