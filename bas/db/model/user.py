from sqlalchemy import Table, Column, Integer, String, Sequence, BigInteger, \
        ForeignKey
from sqlalchemy.orm import relationship

from bas.db.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(100))
    twitter_username = Column(String(50))
    level = Column(Integer)
    max_character_level = Column(Integer)
    total_experience = Column(BigInteger)

    character_id = Column(Integer, ForeignKey('characters.id'))
    default_character_id = Column(Integer, ForeignKey('characters.id'))

    games = relationship('Game', secondary='game_users')
    characters = relationship('Character', foreign_keys=[character_id])
    default_character = relationship('Character',
                                     foreign_keys=default_character_id)

    def __init__(self, username, twitter_username=None):
        self.username = username
        self.twitter_username = twitter_username
        self.default_character = None

    def __repr__(self):
        return '''
                <User(id={}, username={}, twitter_username={}, level={},
                default_character={})>
                '''.format(
            self.id, self.username, self.twitter_username, self.level,
            self.default_character
        )

    def __str__(self):
        return self.username

    def get_active_games(self):
        return [game for game in self.games if game.active]
