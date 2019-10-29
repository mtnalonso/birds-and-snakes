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
            return
        if command == 'populate_database':
            populate_all()
            return
        if command == 'help'
            print_usage()
            return
        print('[-] Wrong command!\n')
        print_usage()


    def create_database(self):
        db.create_all()
        populate_all()

def print_usage()
    print('Manager commands:')
    print('\tcreate_database\tInitializes an empty database')
    print('\tpopulate_database\tPopulates the system database with default data')

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
