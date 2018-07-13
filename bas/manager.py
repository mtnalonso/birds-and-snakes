from bas.db.database import db


class Manager:
    def __init__(self):
        pass

    def command(self, command):
        if command == 'create_database':
            self.create_database()

    def create_database(self):
        db.create_all()

