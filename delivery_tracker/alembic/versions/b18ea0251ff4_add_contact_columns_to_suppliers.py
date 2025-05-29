"""Mark contact columns as already added to suppliers

Revision ID: b18ea0251ff4
Revises: 6dd3b33699e4
Create Date: 2025-05-29 22:35:22.200496
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision: str = 'b18ea0251ff4'
down_revision: Union[str, None] = '6dd3b33699e4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """
    Upgrade migration is a no-op because contact columns
    ('contact_name', 'contact_email', 'contact_phone')
    already exist in the 'suppliers' table.
    """
    pass


def downgrade() -> None:
    """
    Downgrade migration removes the contact columns
    from the 'suppliers' table.
    Note: This operation requires database support for DROP COLUMN.
    """
    with op.batch_alter_table("suppliers") as batch_op:
        batch_op.drop_column("contact_name")
        batch_op.drop_column("contact_email")
        batch_op.drop_column("contact_phone")
