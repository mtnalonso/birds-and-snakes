from sqlalchemy import Column, Integer, Sequence, String

from bas.db.database import Base


class Alignment(Base):
    __tablename__ = 'alignments'
    id = Column(Integer, Sequence('alignment_id_seq'), primary_key=True)
    name = Column(String(100))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Alignment(id={}, name={})>'.format(self.id, self.name)
