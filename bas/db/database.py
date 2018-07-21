from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

import bas.config as config


meta = MetaData(naming_convention={
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
})

Base = declarative_base(metadata=meta)


class Database:
    def __init__(self):
        self.database_name = config.database_name
        self.database_engine = config.database_engine
        self.database_credentials = self.__get_database_credentials()
        self.__init_engine()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.Base = Base

    def __get_database_credentials(self):
        if not config.is_dev_mode():
            return '{}:{}@{}:{}'.format(
                config.database.user,
                config.database_password,
                config.database_host,
                config.database_port
            )
        return ''

    def __init_engine(self):
        self.engine = create_engine(
            '{}://{}/{}'.format(self.database_engine,
                                self.database_credentials,
                                self.database_name),
            connect_args={'check_same_thread': False},
            poolclass=StaticPool)

    def create_all(self):
        metadata = self.Base.metadata
        metadata.bind = self.engine
        metadata.create_all(self.engine)

    def first(self, model_class, **kwargs):
        if kwargs:
            results = self.session.query(model_class).filter_by(**kwargs)
            return results.one_or_none()
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


db = Database()
