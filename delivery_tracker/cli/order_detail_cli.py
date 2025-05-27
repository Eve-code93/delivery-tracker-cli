import click
from models.order_detail import OrderDetail
from db.session import SessionLocal

@click.group()
def order_detail_cli():
    """Commands to manage order details."""
    pass

@order_detail_cli.command('create')
@click.option('--order_id', prompt=True, type=int, help='Order ID')
@click.option('--product_id', prompt=True, type=int, help='Product ID')
@click.option('--quantity', prompt=True, type=int, help='Quantity')
def create_order_detail(order_id, product_id, quantity):
    session = SessionLocal()
    try:
        detail = OrderDetail.create(session, order_id, product_id, quantity)
        click.echo(f"Order Detail created: {detail}")
    except Exception as e:
        click.echo(f"Error creating order detail: {e}")
    finally:
        session.close()

@order_detail_cli.command('list')
def list_order_details():
    session = SessionLocal()
    try:
        details = OrderDetail.get_all(session)
        if details:
            for d in details:
                click.echo(d)
        else:
            click.echo("No order details found.")
    finally:
        session.close()

@order_detail_cli.command('delete')
@click.option('--id', prompt=True, type=int, help='Order Detail ID to delete')
def delete_order_detail(id):
    session = SessionLocal()
    try:
        detail = OrderDetail.find_by_id(session, id)
        if not detail:
            click.echo("Order detail not found.")
            return
        detail.delete(session)
        click.echo("Order detail deleted.")
    except Exception as e:
        click.echo(f"Error deleting order detail: {e}")
    finally:
        session.close()

@order_detail_cli.command('find')
@click.option('--id', prompt=True, type=int, help='Order Detail ID to find')
def find_order_detail(id):
    session = SessionLocal()
    try:
        detail = OrderDetail.find_by_id(session, id)
        if detail:
            click.echo(detail)
        else:
            click.echo("Order detail not found.")
    finally:
        session.close()

# Add view related commands as needed...
