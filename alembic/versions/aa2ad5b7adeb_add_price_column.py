"""add price column

Revision ID: aa2ad5b7adeb
Revises: df305d851c2b
Create Date: 2023-01-08 19:39:40.707368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa2ad5b7adeb'
down_revision = 'df305d851c2b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('property_short_info', sa.Column('price', type_=sa.Float, nullable=True), schema='public')


def downgrade() -> None:
    op.drop_column('property_short_info', sa.Column('price', type_=sa.Float, nullable=True), schema='public')
