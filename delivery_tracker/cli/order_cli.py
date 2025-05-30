import click
from datetime import datetime
from models.order import Order
from db.session import SessionLocal

@click.group()
def order_cli():
    """Commands to manage orders."""
    pass

# --- CLI Commands ---

@order_cli.command('create')
@click.option('--total-price', prompt=True, type=int, help='Total price of the order')
@click.option('--employee-id', prompt=True, type=int, help='ID of the employee who handled the order')
@click.option('--customer-id', prompt=True, type=int, help='ID of the customer who placed the order')
@click.option('--time', default=None, help='Datetime of the order (YYYY-MM-DD HH:MM), optional')
def create_order(total_price, employee_id, customer_id, time):
    session = SessionLocal()
    try:
        time_obj = datetime.strptime(time, "%Y-%m-%d %H:%M") if time else None
        order = Order.create(session, total_price, employee_id, customer_id, time_obj)
        click.echo(f"✅ Order created: {order}")
    except Exception as e:
        click.echo(f"❌ Error creating order: {e}")
    finally:
        session.close()

@order_cli.command('list')
def list_orders():
    session = SessionLocal()
    try:
        orders = Order.get_all(session)
        if orders:
            click.echo("📦 All Orders:")
            for o in orders:
                click.echo(o)
        else:
            click.echo("⚠️ No orders found.")
    finally:
        session.close()

@order_cli.command('delete')
@click.option('--id', prompt=True, type=int, help='Order ID to delete')
def delete_order(id):
    session = SessionLocal()
    try:
        order = Order.find_by_id(session, id)
        if not order:
            click.echo("❌ Order not found.")
            return
        order.delete(session)
        click.echo("🗑️ Order deleted.")
    except Exception as e:
        click.echo(f"❌ Error deleting order: {e}")
    finally:
        session.close()

# --- Interactive Functions ---

def create_order_interactive():
    try:
        total_price = int(input("Enter total price: "))
        employee_id = int(input("Enter employee ID: "))
        customer_id = int(input("Enter customer ID: "))
        time_str = input("Enter datetime (YYYY-MM-DD HH:MM), or leave blank for now: ").strip()

        time_obj = datetime.strptime(time_str, "%Y-%m-%d %H:%M") if time_str else None

        session = SessionLocal()
        order = Order.create(session, total_price, employee_id, customer_id, time_obj)
        print(f"✅ Order created: {order}")
    except ValueError:
        print("❌ Invalid number or datetime format.")
    except Exception as e:
        print(f"❌ Error creating order: {e}")
    finally:
        session.close()

def list_orders_interactive():
    session = SessionLocal()
    try:
        orders = Order.get_all(session)
        if orders:
            print("📦 All Orders:")
            for o in orders:
                print(o)
        else:
            print("⚠️ No orders found.")
    finally:
        session.close()

def delete_order_interactive():
    try:
        id = int(input("Enter order ID to delete: "))
    except ValueError:
        print("❌ Invalid ID.")
        return

    session = SessionLocal()
    try:
        order = Order.find_by_id(session, id)
        if not order:
            print("❌ Order not found.")
            return
        order.delete(session)
        print("🗑️ Order deleted.")
    except Exception as e:
        print(f"❌ Error deleting order: {e}")
    finally:
        session.close()
