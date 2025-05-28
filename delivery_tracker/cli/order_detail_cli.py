import click
from models.order_detail import OrderDetail
from db.session import SessionLocal

@click.group()
def order_detail_cli():
    """Commands to manage order details."""
    pass

@order_detail_cli.command('create')
@click.option('--order-id', prompt=True, type=int, help='Order ID')
@click.option('--product-id', prompt=True, type=int, help='Product ID')
def create_order_detail(order_id, product_id):
    session = SessionLocal()
    try:
        detail = OrderDetail.create(session, order_id, product_id)
        click.echo(f"✅ OrderDetail created: {detail}")
    except Exception as e:
        click.echo(f"❌ Error creating order detail: {e}")
    finally:
        session.close()

@order_detail_cli.command('list')
def list_order_details():
    session = SessionLocal()
    try:
        details = OrderDetail.get_all(session)
        if details:
            click.echo("📦 Order Details:")
            for d in details:
                click.echo(d)
        else:
            click.echo("⚠️ No order details found.")
    finally:
        session.close()

@order_detail_cli.command('delete')
@click.option('--id', prompt=True, type=int, help='OrderDetail ID to delete')
def delete_order_detail(id):
    session = SessionLocal()
    try:
        detail = OrderDetail.find_by_id(session, id)
        if not detail:
            click.echo("❌ Order detail not found.")
            return
        detail.delete(session)
        click.echo("🗑️ Order detail deleted.")
    except Exception as e:
        click.echo(f"❌ Error deleting order detail: {e}")
    finally:
        session.close()
