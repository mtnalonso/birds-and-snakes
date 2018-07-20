from sqlalchemy import Column, Integer, Sequence, String

from bas.db.database import db


class Character(db.Base):
    __tablename__ = 'characters'
    id = Column(Integer, Sequence('character_id_seq'), primary_key=True)
    name = Column(String(500))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Character(id={}, name={})>'.format(self.id, self.name)
