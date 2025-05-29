"""Add in_stock column to products

Revision ID: 27f61e29de69
Revises: b18ea0251ff4
Create Date: 2025-05-29 22:52:09.250765
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = '27f61e29de69'
down_revision: Union[str, None] = 'b18ea0251ff4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Drop leftover temp tables from failed previous migrations (SQLite only)
    op.execute("DROP TABLE IF EXISTS _alembic_tmp_orders;")
    op.execute("DROP TABLE IF EXISTS _alembic_tmp_employees;")

    # Fix NULLs before altering NOT NULL constraints on orders
    op.execute("UPDATE orders SET employee_id = 1 WHERE employee_id IS NULL;")
    op.execute("UPDATE orders SET customer_id = 1 WHERE customer_id IS NULL;")

    # Employees table columns to NOT NULL
    with op.batch_alter_table('employees') as batch_op:
        batch_op.alter_column('age',
                              existing_type=sa.INTEGER(),
                              nullable=False)
        batch_op.alter_column('gender',
                              existing_type=sa.VARCHAR(),
                              nullable=False)
        batch_op.alter_column('date_employed',
                              existing_type=sa.DATE(),
                              nullable=False)

    # Orders table: add columns and alter nullable columns
    with op.batch_alter_table('orders') as batch_op:
        batch_op.add_column(sa.Column('total_price', sa.Integer(), nullable=False, server_default='0'))
        batch_op.add_column(sa.Column('time', sa.DateTime(), nullable=True))
        batch_op.alter_column('employee_id',
                              existing_type=sa.INTEGER(),
                              nullable=False)
        batch_op.alter_column('customer_id',
                              existing_type=sa.INTEGER(),
                              nullable=False)
        batch_op.drop_column('description')

    # Add in_stock column to products
    op.add_column('products', sa.Column('in_stock', sa.Integer(), nullable=False, server_default='0'))

    # Alter products columns
    with op.batch_alter_table('products') as batch_op:
        batch_op.alter_column('price',
                              existing_type=sa.FLOAT(),
                              type_=sa.Integer(),
                              existing_nullable=False)
        batch_op.alter_column('supplier_id',
                              existing_type=sa.INTEGER(),
                              nullable=False)

    # Drop contact_info from suppliers
    with op.batch_alter_table('suppliers') as batch_op:
        batch_op.drop_column('contact_info')

    # Remove server defaults now that existing rows are populated
    with op.batch_alter_table('orders') as batch_op:
        batch_op.alter_column('total_price', server_default=None)
    with op.batch_alter_table('products') as batch_op:
        batch_op.alter_column('in_stock', server_default=None)


def downgrade() -> None:
    # Add contact_info back to suppliers
    with op.batch_alter_table('suppliers') as batch_op:
        batch_op.add_column(sa.Column('contact_info', sa.VARCHAR(), nullable=True))

    # Revert products table
    with op.batch_alter_table('products') as batch_op:
        batch_op.alter_column('supplier_id',
                              existing_type=sa.INTEGER(),
                              nullable=True)
        batch_op.alter_column('price',
                              existing_type=sa.Integer(),
                              type_=sa.FLOAT(),
                              existing_nullable=False)
        batch_op.drop_column('in_stock')

    # Revert orders table
    with op.batch_alter_table('orders') as batch_op:
        batch_op.add_column(sa.Column('description', sa.VARCHAR(), nullable=False))
        batch_op.alter_column('customer_id',
                              existing_type=sa.INTEGER(),
                              nullable=True)
        batch_op.alter_column('employee_id',
                              existing_type=sa.INTEGER(),
                              nullable=True)
        batch_op.drop_column('time')
        batch_op.drop_column('total_price')

    # Revert employees table
    with op.batch_alter_table('employees') as batch_op:
        batch_op.alter_column('date_employed',
                              existing_type=sa.DATE(),
                              nullable=True)
        batch_op.alter_column('gender',
                              existing_type=sa.VARCHAR(),
                              nullable=True)
        batch_op.alter_column('age',
                              existing_type=sa.INTEGER(),
                              nullable=True)
