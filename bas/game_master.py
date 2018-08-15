from datetime import datetime
from threading import Thread
from queue import Queue
from uuid import uuid4

from bas.db.database import db
import bas.manager as manager
from bas.nlp.message_handler import MessageHandler


class GameMaster(Thread):
    def __init__(self, system_master):
        Thread.__init__(self)
        self.__id = uuid4().hex
        self.system_master = system_master
        self.queue = Queue()
        self.message_handler = MessageHandler(self)
        self.game = None
        self.game_ready = False
        self.awaiting_more_characters = False
        self.awaiting_start_confirmation = False
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

        if self.awaiting_more_characters:
            response_message = self.add_people_to_game(message)
        elif self.awaiting_start_confirmation:
            response_message = self.start_game_if_ready(message)
        else:
            response_message = self.message_handler.process(message)

        if self.awaiting_more_characters:
            response_message += '\n- Who else wants to join the game?'
            response_message += '\n(tag user / nobody)\n'
        elif self.awaiting_start_confirmation:
            response_message += '\n- Say "yes" when ready to begin.\n'
        else:
            response_message += '\n'
        print(response_message)

    def add_people_to_game(self, message):
        content_message = message.message.split(':')[-1]
        input_elements = content_message.split()
        new_usernames = []
        response = 'Users:\n'

        for element in input_elements:
            if element[0] == '@':
                new_usernames.append(element[1:])

        for username in new_usernames:
            user = manager.get_user_or_create_if_new(username)
            self.game.users.append(user)
            response += '{}\n'.format(user)

        db.update()
        response += 'were added to game:\n{}\n'.format(self.game)

        for user in self.game.users:
            if user.default_character is None:
                response += '{} needs to create a character'.format(
                    user.username
                )

        self.awaiting_more_characters = False
        self.awaiting_start_confirmation = True
        return response

    def start_game_if_ready(self, message):
        if message.message == 'yes':
            if self.game.players_have_characters_set():
                self.awaiting_start_confirmation = False
                return '[+] GAME HAS STARTED'
            else:
                return '[-] Every user must have a character created!'
        return '- How can I help you?'
