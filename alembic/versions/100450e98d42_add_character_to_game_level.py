"""add character to game level

Revision ID: 100450e98d42
Revises: 9d9b16e7c826
Create Date: 2018-08-22 22:47:20.009968+02:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '100450e98d42'
down_revision = '9d9b16e7c826'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.add_column(sa.Column('game_level_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('position_x', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('position_y', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('position_z', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_characters_game_level_id_game_levels'), 'game_levels', ['game_level_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_characters_game_level_id_game_levels'), type_='foreignkey')
        batch_op.drop_column('position_z')
        batch_op.drop_column('position_y')
        batch_op.drop_column('position_x')
        batch_op.drop_column('game_level_id')

    # ### end Alembic commands ###
