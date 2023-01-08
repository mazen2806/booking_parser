"""delete index by uuid

Revision ID: a4181ea880f4
Revises: 39eaf16de415
Create Date: 2022-07-21 14:38:52.704933

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = 'a4181ea880f4'
down_revision = '39eaf16de415'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute('DROP INDEX ix_public_property_short_info_uuid;')


def downgrade() -> None:
    op.execute('CREATE INDEX ix_public_property_short_info_uuid ON public.property_short_info (uuid);')
