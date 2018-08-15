from sqlalchemy import Column, Integer, String, Sequence

from bas.db.database import Base


INIT = 'Initialized game class'
AWAITING_CHARACTERS = 'Awaiting more characters'
AWAITING_START_CONFIRMATION = 'Awaiting start confirmation'


class GameState(Base):
    __tablename__ = 'game_states'
    id = Column(Integer, Sequence('game_state_id_seq'), primary_key=True)
    name = Column(String(100))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<GameState(id={}, name={})>'.format(self.id, self.name)

    def __str__(self):
        return self.name


def awaiting_characters():
    return db.find(GameState, name=AWAITING_CHARACTERS)


def awaiting_start_confirmation():
    return db.find(GameState, name=AWAITING_START_CONFIRMATION)
