import bas.db.model
from bas.db.database import db
from bas.db.model.user import User


class Manager:
    def __init__(self):
        pass

    def command(self, command):
        if command == 'create_database':
            self.create_database()

    def create_database(self):
        db.create_all()


def get_user_or_create_if_new(username):
    user = db.first(User, username=username)
    if user is None:
        user = create_user(username)
        print('\n[+] Created new user:\n{}\n'.format(user))
    return user


def create_user(username):
    user = User(username)
    db.insert(user)
    return db.first(User, username=username)
