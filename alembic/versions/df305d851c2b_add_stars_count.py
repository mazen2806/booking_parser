"""add stars count

Revision ID: df305d851c2b
Revises: 72f82586f341
Create Date: 2023-01-07 21:21:28.980010

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df305d851c2b'
down_revision = '72f82586f341'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('property_short_info', sa.Column('stars_count', type_=sa.Integer, nullable=True), schema='public')


def downgrade() -> None:
    op.drop_column('property_short_info', sa.Column('stars_count', type_=sa.Integer, nullable=True), schema='public')
