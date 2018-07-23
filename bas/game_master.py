import logging
from datetime import datetime
from pprint import pprint
from threading import Thread

from bas.db.database import db
from bas.db.model.game import Game
import bas.config as config
import bas.manager as manager
from bas.nlp.nlp import NLPFactory


logger = logging.getLogger(__name__)


class GameMaster(Thread):
    def __init__(self, queue, interface=None):
        Thread.__init__(self)
        self.queue = queue
        self.active_games = None
        self.nlp_service = NLPFactory.create(config.nlp_session_id)

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
        self.show_nlp_message_information(message)
        self.send_response(response_message)

    def handle_message_command(self, message):
        if message.message == 'create game':
            return self.create_game(message)
        if message.message == 'list games':
            return self.list_games(message)
        if message.message == 'print game':
            return self.print_game(message)
        if 'add people:' in message.message:
            return self.add_people_to_game(message)
        return message

    def show_nlp_message_information(self, message):
        nlp_data = self.nlp_service.get_message_data(message.message)
        pprint(nlp_data)
        return

    def stop(self):
        self.is_running = False

    def send_response(self, message):
        print(message)
        logger.info('Got message [{}]'.format(message))

    def create_game(self, message):
        user = message.user
        game = Game()
        game.users.append(user)
        db.insert(game)
        self.active_games[game.key] = game
        return '\n[+] Created new game\n{}'.format(game)

    def list_games(self, message):
        str_games_list = 'List of games for {}:\n'.format(message.user)
        for game in message.user.games:
            str_games_list += '{}\n'.format(str(game))
        return str_games_list

    def print_game(self, message):
        """
        Print information of the current active game for the user
        """
        raise NotImplementedError

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
