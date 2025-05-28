"""Add supplier and product models

Revision ID: 61690c62e11e
Revises: e07acd484b66
Create Date: 2025-05-27 12:07:31.288177

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import inspect


# revision identifiers, used by Alembic.
revision: str = '61690c62e11e'
down_revision: Union[str, None] = 'e07acd484b66'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("DROP TABLE IF EXISTS _alembic_tmp_customers")

    # Customers table
    with op.batch_alter_table('customers') as batch_op:
        batch_op.alter_column('name',
                              existing_type=sa.VARCHAR(),
                              nullable=False)
        batch_op.alter_column('email',
                              existing_type=sa.VARCHAR(),
                              nullable=False)
        batch_op.create_unique_constraint('uq_customers_email', ['email'])
        batch_op.drop_column('address')
        batch_op.drop_column('phone_number')

    # Employees table - safely alter 'role' with temp table workaround
    # Create temp table with role nullable
    op.execute('''
        CREATE TABLE _alembic_tmp_employees (
            id INTEGER NOT NULL PRIMARY KEY,
            name VARCHAR NOT NULL,
            role VARCHAR
        )
    ''')
    # Copy data with NULL role replaced by 'unknown'
    op.execute('''
        INSERT INTO _alembic_tmp_employees (id, name, role)
        SELECT id, name, COALESCE(role, 'unknown') FROM employees
    ''')
    # Drop original employees table
    op.drop_table('employees')
    # Rename temp table to employees
    op.execute('ALTER TABLE _alembic_tmp_employees RENAME TO employees')

    # Get current columns for employees
    bind = op.get_bind()
    inspector = inspect(bind)
    employees_columns = [col['name'] for col in inspector.get_columns('employees')]

    # Now continue with other employees changes that don't require temp table
    with op.batch_alter_table('employees') as batch_op:
        batch_op.alter_column('name',
                              existing_type=sa.VARCHAR(),
                              nullable=False)
        batch_op.alter_column('role',
                              existing_type=sa.VARCHAR(),
                              nullable=False)
        # Drop columns only if they exist
        if 'date_employed' in employees_columns:
            batch_op.drop_column('date_employed')
        if 'age' in employees_columns:
            batch_op.drop_column('age')
        if 'gender' in employees_columns:
            batch_op.drop_column('gender')

    # Order Details table
    with op.batch_alter_table('order_details') as batch_op:
        batch_op.add_column(sa.Column('quantity', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('price', sa.Float(), nullable=False))

    # Orders table
    with op.batch_alter_table('orders') as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(), nullable=False))
        batch_op.drop_column('time')
        batch_op.drop_column('total_price')

    # Products table
    with op.batch_alter_table('products') as batch_op:
        batch_op.alter_column('name',
                              existing_type=sa.VARCHAR(),
                              nullable=False)
        batch_op.alter_column('price',
                              existing_type=sa.INTEGER(),
                              type_=sa.Float(),
                              nullable=False)
        batch_op.drop_column('type')
        batch_op.drop_column('in_stock')

    # Suppliers table
    with op.batch_alter_table('suppliers') as batch_op:
        batch_op.add_column(sa.Column('contact_info', sa.String(), nullable=True))
        batch_op.alter_column('name',
                              existing_type=sa.VARCHAR(),
                              nullable=False)
        batch_op.drop_column('location')


def downgrade() -> None:
    # Suppliers table
    with op.batch_alter_table('suppliers') as batch_op:
        batch_op.add_column(sa.Column('location', sa.VARCHAR(), nullable=True))
        batch_op.alter_column('name',
                              existing_type=sa.VARCHAR(),
                              nullable=True)
        batch_op.drop_column('contact_info')

    # Products table
    with op.batch_alter_table('products') as batch_op:
        batch_op.add_column(sa.Column('in_stock', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('type', sa.VARCHAR(), nullable=True))
        batch_op.alter_column('price',
                              existing_type=sa.Float(),
                              type_=sa.INTEGER(),
                              nullable=True)
        batch_op.alter_column('name',
                              existing_type=sa.VARCHAR(),
                              nullable=True)

    # Orders table
    with op.batch_alter_table('orders') as batch_op:
        batch_op.add_column(sa.Column('total_price', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('time', sa.DATETIME(), nullable=True))
        batch_op.drop_column('description')

    # Order Details table
    with op.batch_alter_table('order_details') as batch_op:
        batch_op.drop_column('price')
        batch_op.drop_column('quantity')

    # Employees table
    with op.batch_alter_table('employees') as batch_op:
        batch_op.add_column(sa.Column('gender', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('age', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('date_employed', sa.DATE(), nullable=True))
        batch_op.alter_column('role',
                              existing_type=sa.VARCHAR(),
                              nullable=True)
        batch_op.alter_column('name',
                              existing_type=sa.VARCHAR(),
                              nullable=True)

    # Customers table
    with op.batch_alter_table('customers') as batch_op:
        batch_op.add_column(sa.Column('phone_number', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('address', sa.VARCHAR(), nullable=True))
        batch_op.drop_constraint('uq_customers_email', type_='unique')
        batch_op.alter_column('email',
                              existing_type=sa.VARCHAR(),
                              nullable=True)
        batch_op.alter_column('name',
                              existing_type=sa.VARCHAR(),
                              nullable=True)
