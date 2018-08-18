from sqlalchemy import Column, Integer, Sequence, String

from bas.db.database import Base


class Condition(Base):
    __tablename__ = 'conditions'
    id = Column(Integer, Sequence('conditions_id_seq'), primary_key=True)
    name = Column(String(100))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Condition(id={}, name={})>'.format(self.id, self.name)
