import logging
from datetime import datetime
from pprint import pprint
from threading import Thread

from bas.db.database import db
from bas.db.model.game import Game
import bas.manager as manager
from bas.nlp.message_handler import MessageHandler


logger = logging.getLogger(__name__)


class GameMaster(Thread):
    def __init__(self, queue, interface=None):
        Thread.__init__(self)
        self.queue = queue
        self.active_games = None
        self.message_handler = MessageHandler(self)

    def start(self):
        self.load_active_games()
        self.is_running = True
        super().start()

    def load_active_games(self):
        self.active_games = manager.get_active_games()
        pprint(self.active_games)

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

    def process_message(self):
        message = self.queue.get()
        self.print_message(message.message)
        response_message = self.message_handler.process(message)
        print(response_message)

    def print_message(self, message):
        print(message)
        logger.info('Got message [{}]'.format(message))

    def add_people_to_game(self, message):
        # TODO: add try except and rollback
        content_message = message.message.split(':')[-1]
        input_elements = content_message.split()
        new_usernames = []
        response = 'Users:\n'

        for element in input_elements:
            if element[0] == '#':
                game_key = element[1:]
            if element[0] == '@':
                new_usernames.append(element[1:])

        game = db.first(Game, key=game_key)

        for username in new_usernames:
            user = manager.get_user_or_create_if_new(username)
            game.users.append(user)
            response += '{}\n'.format(user)

        db.update()
        response += 'were added to game:\n{}\n'.format(game)
        return response
