from sqlalchemy import Column, Integer, Sequence, String

from bas.db.database import Base


class Gender(Base):
    __tablename__ = 'genders'
    id = Column(Integer, Sequence('gender_id_seq'), primary_key=True)
    gender = Column(String(500))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Gender(id={}, name={})>'.format(self.id, self.name)
