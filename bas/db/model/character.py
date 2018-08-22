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

    max_hit_points = Column(Integer)
    hit_points = Column(Integer)
    speed = Column(Integer)
    strength = Column(Integer)
    dexterity = Column(Integer)
    constitution = Column(Integer)
    wisdom = Column(Integer)
    charisma = Column(Integer)

    gender_id = Column(Integer, ForeignKey('genders.id'))
    pronoun_id = Column(Integer, ForeignKey('pronouns.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    race_id = Column(Integer, ForeignKey('races.id'))
    character_class_id = Column(Integer, ForeignKey('character_classes.id'))
    condition_id = Column(Integer, ForeignKey('conditions.id'))

    gender = relationship('Gender')
    pronoun = relationship('Pronoun')
    user = relationship('User', foreign_keys=user_id,
                        back_populates='characters')
    race = relationship('Race')
    character_class = relationship('CharacterClass')
    condition = relationship('Condition')

    def __init__(self, name, user=None, race=None, character_class=None,
                 level=1, gender=None, pronoun=None):
        self.name = name
        self.user = user
        self.race = race
        self.character_class = character_class
        self.level = level
        self.experience = 0
        self.gender = gender
        self.pronoun = pronoun

    def __repr__(self):
        return '''<Character(id={}, name={}, level={}, experience={},
               health_points={}, speed={}, strength={}, gender={}, pronoun={},
               character_class={}, condition={})>
               '''.format(
            self.id,
            self.name,
            self.level,
            self.experience,
            self.health_points,
            self.speed,
            self.strength,
            self.gender_id,
            self.pronoun_id,
            self.character_class_id,
            self.condition,
        )

    def __str__(self):
        return '{} [{}: {}, user={}]'.format(
            self.name,
            self.character_class,
            self.level,
            self.user
        )
