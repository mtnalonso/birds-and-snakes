from sqlalchemy import Column, Integer, Sequence, String

from bas.db.database import Base


class Pronoun(Base):
    __tablename__ = 'pronouns'
    id = Column(Integer, Sequence('pronoun_id_seq'), primary_key=True)
    pronoun = Column(String(100))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Pronoun(id={}, name={})>'.format(self.id, self.name)
