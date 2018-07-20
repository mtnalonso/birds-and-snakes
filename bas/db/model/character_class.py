from sqlalchemy import Column, Integer, Sequence, String, Text

from bas.db.database import Base


class CharacterClass(Base):
    __tablename__ = 'character_classes'
    id = Column(Integer, Sequence('character_class_id_seq'), primary_key=True)
    name = Column(String(500))
    description = Column(Text)

    def __init__(self, name, description=None):
        self.name = name
        self.description = description

    def __repr__(self):
        return '<CharacterClass(id={}, name={})>'.format(self.id, self.name)
