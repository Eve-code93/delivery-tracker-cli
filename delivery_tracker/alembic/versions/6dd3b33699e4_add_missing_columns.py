from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '6dd3b33699e4'
down_revision = '7ef64fb01c5b'
branch_labels = None
depends_on = None


def upgrade():
    # Drop unique constraint from 'customers.email' using batch mode
    with op.batch_alter_table('customers') as batch_op:
        batch_op.drop_constraint('uq_customers_email', type_='unique')

    # Add new nullable columns to 'employees'
    op.add_column('employees', sa.Column('age', sa.Integer(), nullable=True))
    op.add_column('employees', sa.Column('gender', sa.String(), nullable=True))
    op.add_column('employees', sa.Column('date_employed', sa.Date(), nullable=True))

    # Populate new columns with default values to avoid nulls if needed
    op.execute("UPDATE employees SET age = 0 WHERE age IS NULL")
    op.execute("UPDATE employees SET gender = 'U' WHERE gender IS NULL")
    op.execute("UPDATE employees SET date_employed = '2000-01-01' WHERE date_employed IS NULL")

    # Drop columns from 'order_details' using batch mode (SQLite does not support drop_column directly)
    with op.batch_alter_table('order_details') as batch_op:
        batch_op.drop_column('quantity')
        batch_op.drop_column('price')

    # Alter 'order_id' and 'product_id' to be non-nullable using batch mode
    with op.batch_alter_table('order_details') as batch_op:
        batch_op.alter_column('order_id',
                              existing_type=sa.INTEGER(),
                              nullable=False)
        batch_op.alter_column('product_id',
                              existing_type=sa.INTEGER(),
                              nullable=False)


def downgrade():
    # To downgrade, reverse the upgrade steps:

    # Add back columns to 'order_details' using batch mode
    with op.batch_alter_table('order_details') as batch_op:
        batch_op.add_column(sa.Column('quantity', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('price', sa.FLOAT(), nullable=True))

        batch_op.alter_column('order_id',
                              existing_type=sa.INTEGER(),
                              nullable=True)
        batch_op.alter_column('product_id',
                              existing_type=sa.INTEGER(),
                              nullable=True)

    # Remove added columns from 'employees'
    with op.batch_alter_table('employees') as batch_op:
        batch_op.drop_column('date_employed')
        batch_op.drop_column('gender')
        batch_op.drop_column('age')

    # Recreate unique constraint on 'customers.email'
    with op.batch_alter_table('customers') as batch_op:
        batch_op.create_unique_constraint('uq_customers_email', ['email'])
