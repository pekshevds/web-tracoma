"""added distance to order

Revision ID: 29162144f355
Revises: 2dff4733d1e1
Create Date: 2022-11-04 15:53:01.632882

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29162144f355'
down_revision = '2dff4733d1e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('distance', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.drop_column('distance')

    # ### end Alembic commands ###