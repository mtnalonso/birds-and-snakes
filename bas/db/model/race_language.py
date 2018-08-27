from sqlalchemy import Column, Integer, ForeignKey

from bas.db.database import Base


class RaceLanguage(Base):
    __tablename__ = 'race_languages'
    race_id = Column(Integer, ForeignKey('races.id'), primary_key=True)
    language_id = Column(Integer, ForeignKey('languages.id'),
                         primary_key=True)
