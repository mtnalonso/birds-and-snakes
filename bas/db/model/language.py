from sqlalchemy import Column, Integer, Sequence, String
from sqlalchemy.orm import relationship

from bas.db.database import Base


class Language(Base):
    __tablename__ = 'languages'
    id = Column(Integer, Sequence('language_id_seq'), primary_key=True)
    name = Column(String(100))

    races = relationship('Race', secondary='race_languages')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Language(id={}, name={})>'.format(self.id, self.name)
