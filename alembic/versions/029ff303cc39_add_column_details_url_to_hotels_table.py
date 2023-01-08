"""add column details_url to hotels table

Revision ID: 029ff303cc39
Revises: b38da3426100
Create Date: 2022-08-01 22:58:15.010412

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '029ff303cc39'
down_revision = 'b38da3426100'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('property_short_info', sa.Column('details_url', type_=sa.String(500), nullable=True), schema='public')


def downgrade() -> None:
    op.drop_column('property_short_info', sa.Column('details_url', type_=sa.String(500), nullable=True), schema='public')
