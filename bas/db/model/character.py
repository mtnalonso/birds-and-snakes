from sqlalchemy import Column, Integer, Sequence, String, ForeignKey, \
        BigInteger
from sqlalchemy.orm import relationship

from bas.db.database import Base


class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, Sequence('character_id_seq'), primary_key=True)
    name = Column(String(500))
    level = Column(Integer)
    experience = Column(BigInteger)
    health_points = Column(Integer)
    speed = Column(Integer)
    strength = Column(Integer)
    intelligence = Column(Integer)

    gender = relationship('Gender')
    pronoun = relationship('Pronoun')
    character_class = relationship('CharacterClass')

    gender_id = Column(Integer, ForeignKey('genders.id'))
    pronoun_id = Column(Integer, ForeignKey('pronouns.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    character_class_id = Column(Integer, ForeignKey('character_classes.id'))

    def __init__(self, name, level=1, gender=None, pronoun=None):
        self.name = name
        self.level = level
        self.experience = 0
        self.gender = gender
        self.pronoun = pronoun

    def __repr__(self):
        return '''<Character(id={}, name={}, level={}, experience={},
               health_points={}, speed={}, strength={}, intelligence={},
               gender={}, pronoun={}, character_class={})>
               '''.format(
            self.id,
            self.name,
            self.level,
            self.experience,
            self.health_points,
            self.speed,
            self.strength,
            self.intelligence,
            self.gender_id,
            self.pronoun_id,
            self.character_class_id,
        )
