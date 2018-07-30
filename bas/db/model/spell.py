from sqlalchemy import Column, Integer, Sequence, String, ForeignKey
from sqlalchemy.orm import relationship

from bas.db.database import Base


class Spell(Base):
    __tablename__ = 'spells'
    id = Column(Integer, Sequence('spell_id_seq'), primary_key=True)
    name = Column(String(500))
    level = Column(Integer)

    character_class = relationship('CharacterClass')
    school = relationship('MagicSchool')

    character_class_id = Column(Integer, ForeignKey('character_classes.id'))
    school_id = Column(Integer, ForeignKey('magic_schools.id'))

    def __init__(self, name, level=0, character_class=None, school=None):
        self.name = name
        self.level = level
        self.character_class = character_class
        self.school = school

    def __repr__(self):
        return '''<Spell(id={}, name={}, level={}, character_class={},
                school={})>'''.format(
            self.id,
            self.name,
            self.level,
            self.character_class,
            self.school
        )
