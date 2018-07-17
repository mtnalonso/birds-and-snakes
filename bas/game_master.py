import logging
from datetime import datetime
from pprint import pprint
from threading import Thread

from bas.game import Game
from bas.player import Player
from bas.db.database import db
import bas.db.model as model


logger = logging.getLogger(__name__)


class GameMaster(Thread):
    def __init__(self, queue, interface=None):
        Thread.__init__(self)
        self.queue = queue
        self.active_games = None

    def start(self):
        self.load_active_games()
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

    def load_active_games(self):
        self.active_games = {}
        print('[-] Warning: not loading active games from DB\n')

    def process_message(self):
        message = self.queue.get()
        response_message = self.handle_message_command(message)
        self.send_response(response_message)

    def handle_message_command(self, message):
        if message.message == 'create game':
            return self.create_game(message)
        if message.message == 'list games':
            return self.list_games(message)
        if message.message == 'print game':
            return self.print_game(message)
        if message.message == 'add people':
            return self.add_people(message)
        return message

    def stop(self):
        self.is_running = False

    def send_response(self, message):
        print(message)
        logger.info('Got message [{}]'.format(message))

    def create_game(self, message):
        user = message.user
        game = model.Game()
        game.users.append(user)
        db.insert(game)
        self.active_games[game.key] = game
        return '\n[+] Created new game\n{}'.format(game)

    def list_games(self):
        str_games_list = '\n'
        user = db.first(model.User, username=message.user)
        for game in db.all(model.Game, user=user):
            str_games_list += '{}\n'.format(str(game))
        return str_games_list

    def print_game(self, message):
        """
        Print information of the current active game for the user
        """
        raise NotImplementedError

    def add_people_to_game(self, message):
        """
        Add other people to your active game separated by commas
        If there is no active game, notice to create one
        Game key on message
        """
        raise NotImplementedError
