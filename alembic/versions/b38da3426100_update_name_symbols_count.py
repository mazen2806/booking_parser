"""update name symbols count

Revision ID: b38da3426100
Revises: 0368a415ca31
Create Date: 2022-07-30 21:26:42.832362

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b38da3426100'
down_revision = '0368a415ca31'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('property_short_info', 'name',
                    existing_type=sa.VARCHAR(length=100),
                    type_=sa.String(length=200),
                    existing_nullable=False)


def downgrade() -> None:
    op.alter_column('property_short_info', 'name',
                    existing_type=sa.VARCHAR(length=200),
                    type_=sa.String(length=100),
                    existing_nullable=False)
