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
    pronoun_id = Column(Integer, ForeignKey('pronouns.id'))
    pronoun = relationship('Pronoun')
    level = Column(Integer)
    experience = Column(BigInteger)

    def __init__(self, name, gender=None, pronoun=None, level=1):
        self.name = name
        self.gender = gender
        self.pronoun = pronoun
        self.level = level
        self.experience = 0

    def __repr__(self):
        return '''<Character(id={}, name={}, gender={}, pronoun={}, level={},
               experience={})>
               '''.format(
            self.id,
            self.name,
            self.gender,
            self.pronoun,
            self.level,
            self.experience,
        )
