from sqlalchemy import Table, Column
from database import Base


game_users = Table('game_users', Base.metadata,
    Column('game_id', ForeignKey('games.id'), primary_key=True),
    Column('keyword_id', ForeignKey('keywords.id'), primary_key=True)
)
