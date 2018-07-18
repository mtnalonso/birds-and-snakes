from sqlalchemy import Column, Integer, ForeignKey

from bas.db.database import db


class GameUsers(db.Base):
    __tablename__ = 'game_users'
    game_id = Column(Integer, ForeignKey('games.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
