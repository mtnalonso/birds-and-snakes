from sqlalchemy import Column, Integer, Sequence, String

from bas.db.database import Base


class Race(Base):
    __tablename__ = 'races'
    id = Column(Integer, Sequence('race_id_seq'), primary_key=True)
    name = Column(String(100))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Race(id={}, name={})>'.format(self.id, self.name)
