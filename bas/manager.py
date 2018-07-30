from pprint import pprint

import bas.db.model
from bas.db.database import db
from bas.db.model.user import User
from bas.db.model.game import Game
from bas.db.scripts.base_database import populate_all


class Manager:
    def __init__(self):
        pass

    def command(self, command):
        if command == 'create_database':
            self.create_database()

    def create_database(self):
        db.create_all()
        populate_all()


def get_user_or_create_if_new(username):
    user = db.find(User, username=username)
    if user is None:
        user = create_user(username)
        print('\n[+] Created new user:\n{}\n'.format(user))
    return user


def create_user(username):
    user = User(username)
    db.insert(user)
    return db.find(User, username=username)


def get_active_games():
    active_games = {}
    for game in db.all(Game, active=True):
        active_games[game.key] = game
    return active_games
