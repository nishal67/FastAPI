"""add content to posts table

Revision ID: 046687ee091a
Revises: ff3b53362bd2
Create Date: 2023-08-05 17:31:09.156926

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '046687ee091a'
down_revision: Union[str, None] = 'ff3b53362bd2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
