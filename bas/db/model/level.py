from sqlalchemy import Column, Integer, Sequence, String, ForeignKey
from sqlalchemy.orm import relationship

from bas.db.database import Base


class Level(Base):
    __tablename__ = 'levels'
    id = Column(Integer, Sequence('level_id_seq'), primary_key=True)
    name = Column(String(200))

    story_id = Column(Integer, ForeignKey('stories.id'))

    story = relationship('Story', foreign_keys=story_id)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Level(id={}, name={})>'.format(self.id, self.name)

    def __str__(self):
        return self.name
