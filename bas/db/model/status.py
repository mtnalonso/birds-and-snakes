from sqlalchemy import Column, Integer, Sequence, String

from bas.db.database import Base


class Status(Base):
    __tablename__ = 'statuses'
    id = Column(Integer, Sequence('status_id_seq'), primary_key=True)
    name = Column(String(100))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Status(id={}, name={})>'.format(self.id, self.name)
