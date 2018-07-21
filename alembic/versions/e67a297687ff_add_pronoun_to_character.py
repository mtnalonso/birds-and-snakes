"""add pronoun to character

Revision ID: e67a297687ff
Revises: e761bdcbe7d0
Create Date: 2018-07-21 01:03:37.224259+02:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e67a297687ff'
down_revision = 'e761bdcbe7d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pronoun_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_characters_pronoun_id_pronouns'), 'pronouns', ['pronoun_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_characters_pronoun_id_pronouns'), type_='foreignkey')
        batch_op.drop_column('pronoun_id')

    # ### end Alembic commands ###