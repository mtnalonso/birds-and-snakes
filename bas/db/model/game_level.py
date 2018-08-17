from sqlalchemy import Column, Integer, Sequence, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from bas.db.database import Base


class GameLevel(Base):
    __tablename__ = 'game_levels'
    id = Column(Integer, Sequence('game_level_id_seq'), primary_key=True)
    active = Column(Boolean(name='active_bool'))

    level_id = Column(Integer, ForeignKey('levels.id'))
    game_id = Column(Integer, ForeignKey('games.id'))

    level = relationship('Level', foreign_keys=level_id)
    game = relationship('Game', foreign_keys=game_id)
    user_characters = relationship('GameLevelCharacter')

    def __init__(self, active=False, level=None, game=None):
        self.active = active
        self.level = level
        self.game = game

    def __repr__(self):
        return '<GameLevel(id={}, level={}, game={})>'.format(
            self.id, self.level, self.game
        )
