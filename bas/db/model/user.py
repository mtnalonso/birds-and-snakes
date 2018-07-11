from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from bas.db.database import Base
from bas.db.model.game_users import game_users


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    twitter_username = Column(String)
    games = relationship(
        'Game',
        secondary=association_table,
        back_poputales='users'
    )
    
    def __init__(self, username, twitter_username=None):
        self.username = username
        self.twitter_username = twitter_username

    def __repr__(self):
        return '<User(id={}, username={}, twitter_username={})>'.format(
                self.id, self.username, self.twitter_username
        )
