"""create hotels table

Revision ID: 39eaf16de415
Revises: 
Create Date: 2022-07-20 18:27:05.962212

"""
import sqlalchemy as sa

from alembic import op
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = '39eaf16de415'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute('CREATE SCHEMA IF NOT EXISTS public;')
    op.create_table(
        'property_short_info',
        sa.Column('uuid', UUID(as_uuid=True), primary_key=True, unique=True, index=True, nullable=False, default=uuid4),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('score', sa.Float(5, 2), nullable=False),
        sa.Column('city', sa.String(50), nullable=False),
        sa.PrimaryKeyConstraint('uuid'),
        schema='public'
    )


def downgrade() -> None:
    op.execute('DROP TABLE property_short_info;')
    op.execute('DROP SCHEMA IF NOT EXISTS public;')
