import click
from cli import customer_cli, employee_cli, order_cli, order_detail_cli, product_cli

@click.group()
def cli():
    """Delivery Tracker CLI Application."""
    pass

# Register subcommands
cli.add_command(customer_cli.customer_cli)
cli.add_command(employee_cli.employee_cli)
cli.add_command(order_cli.order_cli)
cli.add_command(order_detail_cli.order_detail_cli)
cli.add_command(product_cli.product_cli)

if __name__ == '__main__':
    while True:
        try:
            cli()
            # After a command finishes, prompt again until user exits
        except (KeyboardInterrupt, EOFError):
            print("\nExiting Delivery Tracker CLI. Goodbye!")
            break
