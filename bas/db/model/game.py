from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, Integer, String, DateTime, Sequence, Boolean
from sqlalchemy.orm import relationship

from bas.db.database import Base


class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, Sequence('game_id_seq'), primary_key=True)
    key = Column(String(50))
    creation_datetime = Column(DateTime)
    active = Column(Boolean)
    last_message_datetime = Column(DateTime)

    users = relationship('User', secondary='game_users')

    def __init__(self, active=True):
        self.creation_datetime = datetime.now()
        self.key = uuid4().hex
        self.active = active

    def __repr__(self):
        return '<Game(id={}, key={}, active={})>'.format(
            self.id, self.key, self.active
        )
