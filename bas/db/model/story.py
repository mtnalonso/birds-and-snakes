from sqlalchemy import Column, Integer, Sequence, String, ForeignKey, Text
from sqlalchemy.orm import relationship

from bas.db.database import Base


class Story(Base):
    __tablename__ = 'stories'
    id = Column(Integer, Sequence('story_id_seq'), primary_key=True)
    name = Column(String(100))
    introduction = Column(Text)

    start_level_id = Column(Integer, ForeignKey('levels.id'))

    start_level = relationship('Level', foreign_keys=start_level_id)

    def __init__(self, name, introduction=None):
        self.name = name
        self.introduction = introduction

    def __repr__(self):
        return '<Story(id={}, name={})>'.format(self.id, self.name)

    def __str__(self):
        return self.name
