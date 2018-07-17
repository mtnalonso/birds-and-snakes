from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, Sequence('game_id_seq'), primary_key=True)
    key = Column(String(50))
    datetime = Column(DateTime)
    last_message_data = Column(DateTime)
    users = relationship('User', secondary='game_users')

    def __init__(self):
        self.datetime = datetime.now()

    def __repr__(self):
        return '<Game(id={})>'.format(self.id)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(100))
    twitter_username = Column(String(50))
    games = relationship('Game', secondary='game_users')
    
    def __init__(self, username, twitter_username=None):
        self.username = username
        self.twitter_username = twitter_username

    def __repr__(self):
        return '<User(id={}, username={}, twitter_username={})>'.format(
                self.id, self.username, self.twitter_username
        )


class GameUsers(Base):
    __tablename__ = 'game_users'
    game_id = Column(Integer, ForeignKey('games.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)


metadata = Base.metadata
