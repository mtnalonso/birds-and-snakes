from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from bas.db.database import Base


class GameLevelCharacter(Base):
    __tablename__ = 'game_level_characters'
    game_level_id = Column(Integer, ForeignKey('game_levels.id'),
                           primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.id'),
                          primary_key=True)
    position_x = Column(Integer)
    position_y = Column(Integer)
    position_z = Column(Integer)

    character = relationship('Character')
