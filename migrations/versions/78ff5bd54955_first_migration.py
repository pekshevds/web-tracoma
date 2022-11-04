"""first migration

Revision ID: 78ff5bd54955
Revises: 
Create Date: 2022-10-29 08:28:40.340559

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78ff5bd54955'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('point',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=150), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('update_date', sa.DateTime(), nullable=True),
    sa.Column('short', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('storage',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=150), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('update_date', sa.DateTime(), nullable=True),
    sa.Column('is_internal', sa.Boolean(), nullable=True),
    sa.Column('is_employee', sa.Boolean(), nullable=True),
    sa.Column('kind', sa.Integer(), nullable=False),
    sa.Column('inn', sa.String(length=13), nullable=True),
    sa.Column('kpp', sa.String(length=10), nullable=True),
    sa.Column('weight', sa.Float(), nullable=True),
    sa.Column('volume', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cargo_movement',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=150), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('update_date', sa.DateTime(), nullable=True),
    sa.Column('shipper_id', sa.Integer(), nullable=True),
    sa.Column('consignee_id', sa.Integer(), nullable=True),
    sa.Column('cost', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['consignee_id'], ['storage.id'], ),
    sa.ForeignKeyConstraint(['shipper_id'], ['storage.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('issuance_of_cargo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=150), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('update_date', sa.DateTime(), nullable=True),
    sa.Column('storage_id', sa.Integer(), nullable=True),
    sa.Column('cost', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['storage_id'], ['storage.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=150), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('update_date', sa.DateTime(), nullable=True),
    sa.Column('carrier_id', sa.Integer(), nullable=False),
    sa.Column('consignee_id', sa.Integer(), nullable=False),
    sa.Column('consignee_address', sa.String(length=255), nullable=True),
    sa.Column('consignee_contact_id', sa.Integer(), nullable=True),
    sa.Column('consignee_phone', sa.String(length=255), nullable=True),
    sa.Column('declared', sa.Float(), nullable=True),
    sa.Column('desc', sa.Text(), nullable=True),
    sa.Column('point_from_id', sa.Integer(), nullable=False),
    sa.Column('point_to_id', sa.Integer(), nullable=False),
    sa.Column('shipper_id', sa.Integer(), nullable=False),
    sa.Column('shipper_address', sa.String(length=255), nullable=True),
    sa.Column('shipper_contact_id', sa.Integer(), nullable=True),
    sa.Column('shipper_phone', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['carrier_id'], ['storage.id'], ),
    sa.ForeignKeyConstraint(['consignee_contact_id'], ['storage.id'], ),
    sa.ForeignKeyConstraint(['consignee_id'], ['storage.id'], ),
    sa.ForeignKeyConstraint(['point_from_id'], ['point.id'], ),
    sa.ForeignKeyConstraint(['point_to_id'], ['point.id'], ),
    sa.ForeignKeyConstraint(['shipper_contact_id'], ['storage.id'], ),
    sa.ForeignKeyConstraint(['shipper_id'], ['storage.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('receipt_of_cargo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=150), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('update_date', sa.DateTime(), nullable=True),
    sa.Column('storage_id', sa.Integer(), nullable=True),
    sa.Column('cost', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['storage_id'], ['storage.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('attachment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('update_date', sa.DateTime(), nullable=True),
    sa.Column('weight', sa.Float(), nullable=True),
    sa.Column('volume', sa.Float(), nullable=True),
    sa.Column('height', sa.Float(), nullable=True),
    sa.Column('width', sa.Float(), nullable=True),
    sa.Column('depth', sa.Float(), nullable=True),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('attachment_cargo_movement',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('update_date', sa.DateTime(), nullable=True),
    sa.Column('movement_id', sa.Integer(), nullable=True),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['movement_id'], ['cargo_movement.id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('attachment_issuance_of_cargo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('update_date', sa.DateTime(), nullable=True),
    sa.Column('issuance_id', sa.Integer(), nullable=True),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['issuance_id'], ['issuance_of_cargo.id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('attachment_receipt_of_cargo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('update_date', sa.DateTime(), nullable=True),
    sa.Column('receipt_id', sa.Integer(), nullable=True),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.ForeignKeyConstraint(['receipt_id'], ['receipt_of_cargo.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('attachment_receipt_of_cargo')
    op.drop_table('attachment_issuance_of_cargo')
    op.drop_table('attachment_cargo_movement')
    op.drop_table('attachment')
    op.drop_table('receipt_of_cargo')
    op.drop_table('order')
    op.drop_table('issuance_of_cargo')
    op.drop_table('cargo_movement')
    op.drop_table('storage')
    op.drop_table('point')
    # ### end Alembic commands ###
