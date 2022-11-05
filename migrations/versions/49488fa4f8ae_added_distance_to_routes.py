"""added distance to routes

Revision ID: 49488fa4f8ae
Revises: abf06dc0d08c
Create Date: 2022-11-04 12:05:59.404862

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49488fa4f8ae'
down_revision = 'abf06dc0d08c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('route', schema=None) as batch_op:
        batch_op.add_column(sa.Column('distance', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('route', schema=None) as batch_op:
        batch_op.drop_column('distance')

    # ### end Alembic commands ###