"""update score column for hotels

Revision ID: 0368a415ca31
Revises: a4181ea880f4
Create Date: 2022-07-30 10:43:30.509147

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0368a415ca31'
down_revision = 'a4181ea880f4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('property_short_info', 'score', nullable=True)


def downgrade() -> None:
    op.alter_column('property_short_info', 'score', nullable=False)
