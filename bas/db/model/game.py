from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, Integer, String, DateTime, Sequence, Boolean, \
        ForeignKey
from sqlalchemy.orm import relationship

from bas.db.database import Base


class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, Sequence('game_id_seq'), primary_key=True)
    key = Column(String(50))
    creation_datetime = Column(DateTime)
    active = Column(Boolean(name='active_bool'))
    last_message_datetime = Column(DateTime)
    
    state_id = Column(Integer, ForeignKey('game_states.id'))

    state = relationship('GameState', foreign_keys=state_id)
    users = relationship('User', secondary='game_users')

    def __init__(self, active=True):
        self.creation_datetime = datetime.now()
        self.key = uuid4().hex
        self.active = active

    def __repr__(self):
        return '<Game(id={}, key={}, active={}, state={})>'.format(
            self.id, self.key, self.active, self.state
        )
