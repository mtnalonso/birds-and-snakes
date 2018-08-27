from sqlalchemy import Column, Integer, Sequence, String
from sqlalchemy.orm import relationship

from bas.db.database import Base


class Race(Base):
    __tablename__ = 'races'
    id = Column(Integer, Sequence('race_id_seq'), primary_key=True)
    name = Column(String(100))
    speed = Column(Integer)

    languages = relationship('Language', secondary='race_languages')

    def __init__(self, name, speed=None):
        self.name = name
        self.speed = speed

    def __repr__(self):
        return '<Race(id={}, name={})>'.format(self.id, self.name)
