"""update details url column 

Revision ID: 72f82586f341
Revises: 029ff303cc39
Create Date: 2022-08-01 23:21:11.876025

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72f82586f341'
down_revision = '029ff303cc39'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('property_short_info', 'details_url',
                    existing_type=sa.VARCHAR(length=500),
                    type_=sa.String(length=700),
                    existing_nullable=True)


def downgrade() -> None:
    op.alter_column('property_short_info', 'details_url',
                    existing_type=sa.VARCHAR(length=700),
                    type_=sa.String(length=500),
                    existing_nullable=True)
