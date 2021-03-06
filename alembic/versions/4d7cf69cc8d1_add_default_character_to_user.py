"""add default character to user

Revision ID: 4d7cf69cc8d1
Revises: dcfd2ebb1f8d
Create Date: 2018-08-13 22:42:58.292506+02:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d7cf69cc8d1'
down_revision = 'dcfd2ebb1f8d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('default_character_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_users_default_character_id_characters'), 'characters', ['default_character_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_users_default_character_id_characters'), type_='foreignkey')
        batch_op.drop_column('default_character_id')

    # ### end Alembic commands ###
