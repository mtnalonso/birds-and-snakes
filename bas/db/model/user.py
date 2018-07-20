from sqlalchemy import Table, Column, Integer, String, Sequence
from sqlalchemy.orm import relationship

from bas.db.database import Base


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

    def get_active_games(self):
        return [game for game in self.games if game.active]
