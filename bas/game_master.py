import logging
from datetime import datetime
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
        self.games = {}
        self.user_games = {}

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

    def process_message(self):
        message = self.queue.get()
        response = self.handle_message_command(message)
        self.send_response(response)

    def handle_message_command(self, message):
        if message.message == 'create game':
            return self.create_game(message)
        if message.message == 'list games':
            return self.list_games(message)
        if message.message == 'print game':
            return self.print_game(message)
        return message

    def stop(self):
        self.is_running = False

    def send_response(self, response):
        print(response)
        logger.info('Got message [{}]'.format(response))

    def create_game(self, message):
        username = message.username
        character_name = message.username
        game_key = '{}-{}'.format(datetime.now(), username)

        game = Game(game_key)
        player = Player(username, character_name)
        game.add_player(player)

        self.games[game_key] = game
        if username in self.user_games:
            self.user_games[username].append(game_key)
        else:
            self.user_games[username] = []
            self.user_games[username].append(game_key)
        return 'GAME CREATED: {}'.format(game.key)

    def list_games(self):
        str_games_list = '\n'
        user = db.first(model.User, username=message.user)
        for game in db.all(model.Game, user=user):
            str_games_list += '{}\n'.format(str(game))
        return str_games_list

    def print_game(self, message):
        game_key = self.user_games[message.user][0]
        game = self.games[game_key]
        return game.print_levels()
