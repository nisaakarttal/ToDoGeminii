"""phone number added

Revision ID: 399bbb87733b
Revises: 
Create Date: 2026-03-21 16:39:42.110289

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '399bbb87733b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))


def downgrade() -> None:
    pass
