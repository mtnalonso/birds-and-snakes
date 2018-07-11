from datetime import datetime

from sqlalchemy import Column, Integer, String, Time
from sqlalchemy.orm import relationship

from bas.db.database import Base
from bas.db.model.game_users import game_users


class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    datetime = Column(Time)
    users = relationship(
        'User',
        secondary=association_table,
        back_populates='games'
    )

    def __init__(self):
        self.datetime = datetime.now()

    def __repr__(self):
        return '<Game(id={})>'.format(self.id)
