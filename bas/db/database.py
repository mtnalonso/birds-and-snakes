from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Database:
    def __init__(self, database_name):
        self.database_name = database_name
        self.engine = create_engine('sqlite:///{}.db'.format(database_name))
        Session = sessionmaker()
        Session.configure(bind=self.engine)
        self.session = Session()


db = Database()
