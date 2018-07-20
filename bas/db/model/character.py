from sqlalchemy import Column, Integer, Sequence, String, ForeignKey, \
        BigInteger
from sqlalchemy.orm import relationship

from bas.db.database import Base


class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, Sequence('character_id_seq'), primary_key=True)
    name = Column(String(500))
    gender_id = Column(Integer, ForeignKey('genders.id'))
    gender = relationship('Gender')
    experience = Column(BigInteger)
    level = Column(Integer)

    def __init__(self, name, gender=None, level=1):
        self.name = name
        self.gender = gender
        self.level = level

    def __repr__(self):
        return '<Character(id={}, name={}, gender={})>'.format(
            self.id,
            self.name,
            self.gender,
        )
