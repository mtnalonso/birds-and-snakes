from bas.db.database import db
from bas.db.model import User


class Manager:
    def __init__(self):
        pass

    def command(self, command):
        if command == 'create_database':
            self.create_database()

    def create_database(self):
        db.create_all()


def create_user(username):
    user = User(username)
    db.insert(user)
    return db.first(User, username=username)
