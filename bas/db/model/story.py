from sqlalchemy import Column, Integer, Sequence, String
from sqlalchemy.orm import relationship

from bas.db.database import Base


class Story(Base):
    __tablename__ = 'stories'
    id = Column(Integer, Sequence('story_id_seq'), primary_key=True)
    name = Column(String(100))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Story(id={}, name={})>'.format(self.id, self.name)

    def __str__(self):
        return self.name
