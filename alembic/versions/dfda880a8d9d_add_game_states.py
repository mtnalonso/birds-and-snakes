"""add game states

Revision ID: dfda880a8d9d
Revises: 4d7cf69cc8d1
Create Date: 2018-08-15 20:04:49.402421+02:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dfda880a8d9d'
down_revision = '4d7cf69cc8d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game_states',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_game_states'))
    )
    with op.batch_alter_table('games', schema=None) as batch_op:
        batch_op.add_column(sa.Column('state_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_games_state_id_game_states'), 'game_states', ['state_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('games', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_games_state_id_game_states'), type_='foreignkey')
        batch_op.drop_column('state_id')

    op.drop_table('game_states')
    # ### end Alembic commands ###
