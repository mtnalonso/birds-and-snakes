"""add condition to character

Revision ID: 9f1ee870ce77
Revises: b2e8de68f324
Create Date: 2018-08-18 02:02:20.336633+02:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f1ee870ce77'
down_revision = 'b2e8de68f324'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.add_column(sa.Column('condition_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_characters_condition_id_conditions'), 'conditions', ['condition_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_characters_condition_id_conditions'), type_='foreignkey')
        batch_op.drop_column('condition_id')

    # ### end Alembic commands ###
