import click

# Import CLI groups
from cli.customer_cli import customer_cli
from cli.employee_cli import employee_cli
from cli.order_cli import order_cli
from cli.order_detail_cli import order_detail_cli
from cli.product_cli import product_cli
from cli.supplier_cli import supplier_cli

@click.group()
def cli():
    """Delivery Tracker CLI - Manage customers, employees, orders, and more."""
    pass

# Register subcommands
cli.add_command(customer_cli, name='customer-cli')
cli.add_command(employee_cli, name='employee-cli')
cli.add_command(order_cli, name='order-cli')
cli.add_command(order_detail_cli, name='order-detail-cli')
cli.add_command(product_cli, name='product-cli')
cli.add_command(supplier_cli, name='supplier-cli')

if __name__ == '__main__':
    cli()
