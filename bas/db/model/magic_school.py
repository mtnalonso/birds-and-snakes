from sqlalchemy import Column, Integer, Sequence, String

from bas.db.database import Base


class MagicSchool(Base):
    __tablename__ = 'magic_schools'
    id = Column(Integer, Sequence('magic_school_id_seq'), primary_key=True)
    name = Column(String(500))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<MagicSchool(id={}, name={})>'.format(self.id, self.name)

    def __str__(self):
        return self.name
