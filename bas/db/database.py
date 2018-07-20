from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool


Base = declarative_base()


class Database:
    def __init__(self, database_name):
        self.database_name = database_name
        self.engine = create_engine('sqlite:///{}.sqlite'.format(database_name),
                connect_args={'check_same_thread':False},
                poolclass=StaticPool)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.Base = Base

    def create_all(self):
        metadata = self.Base.metadata
        metadata.bind = self.engine
        metadata.create_all(self.engine)

    def first(self, model_class, **kwargs):
        if kwargs:
            return self.session.query(model_class).filter_by(**kwargs).one_or_none()
        return self.session.query(model_class).one_or_none()

    def all(self, model_class, **kwargs):
        if kwargs:
            return self.session.query(model_class).filter_by(**kwargs).all()
        return self.session.query(model_class).all()

    def insert(self, entity):
        self.session.add(entity)
        self.session.commit()

    def update(self):
        self.session.commit()


db = Database('database_bas')
