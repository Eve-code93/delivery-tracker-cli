import click
from models.order import Order
from db.session import SessionLocal

@click.group()
def order_cli():
    """Commands to manage orders."""
    pass

@order_cli.command('create')
@click.option('--customer_id', prompt=True, type=int, help='Customer ID')
@click.option('--employee_id', prompt=True, type=int, help='Employee ID')
def create_order(customer_id, employee_id):
    session = SessionLocal()
    try:
        order = Order.create(session, customer_id, employee_id)
        click.echo(f"Order created: {order}")
    except Exception as e:
        click.echo(f"Error creating order: {e}")
    finally:
        session.close()

@order_cli.command('list')
def list_orders():
    session = SessionLocal()
    try:
        orders = Order.get_all(session)
        if orders:
            for o in orders:
                click.echo(o)
        else:
            click.echo("No orders found.")
    finally:
        session.close()

@order_cli.command('delete')
@click.option('--id', prompt=True, type=int, help='Order ID to delete')
def delete_order(id):
    session = SessionLocal()
    try:
        order = Order.find_by_id(session, id)
        if not order:
            click.echo("Order not found.")
            return
        order.delete(session)
        click.echo("Order deleted.")
    except Exception as e:
        click.echo(f"Error deleting order: {e}")
    finally:
        session.close()

@order_cli.command('find')
@click.option('--id', prompt=True, type=int, help='Order ID to find')
def find_order(id):
    session = SessionLocal()
    try:
        order = Order.find_by_id(session, id)
        if order:
            click.echo(order)
        else:
            click.echo("Order not found.")
    finally:
        session.close()

# Add view related commands as needed...
