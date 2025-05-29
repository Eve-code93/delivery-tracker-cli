import click
from models.customer import Customer
from db.session import SessionLocal

# ---- Click CLI commands (optional terminal usage) ----

@click.group()
def customer_cli():
    """Commands to manage customers."""
    pass

@customer_cli.command('create')
@click.option('--name', prompt=True)
@click.option('--address', prompt=True)
@click.option('--phone-number', prompt=True)
@click.option('--email', prompt=True)
def create_customer(name, address, phone_number, email):
    session = SessionLocal()
    try:
        customer = Customer.create(session, name, address, phone_number, email)
        click.echo(f"✅ Customer created: {customer}")
    except Exception as e:
        click.echo(f"❌ Error creating customer: {e}")
    finally:
        session.close()

@customer_cli.command('list')
def list_customers():
    session = SessionLocal()
    try:
        customers = Customer.get_all(session)
        if customers:
            for c in customers:
                click.echo(c)
        else:
            click.echo("No customers found.")
    finally:
        session.close()

@customer_cli.command('delete')
@click.option('--id', prompt=True, type=int)
def delete_customer(id):
    session = SessionLocal()
    try:
        customer = Customer.find_by_id(session, id)
        if not customer:
            click.echo("Customer not found.")
            return
        customer.delete(session)
        click.echo("🗑️ Customer deleted.")
    except Exception as e:
        click.echo(f"❌ Error deleting customer: {e}")
    finally:
        session.close()

@customer_cli.command('find')
@click.option('--name', prompt=True)
def find_customer(name):
    session = SessionLocal()
    try:
        results = Customer.find_by_name(session, name)
        if results:
            for c in results:
                click.echo(c)
        else:
            click.echo("No customers matched your search.")
    finally:
        session.close()


# ---- Interactive versions (for main menu integration) ----

def create_customer_interactive():
    name = input("Enter name: ").strip()
    address = input("Enter address: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    session = SessionLocal()
    try:
        customer = Customer.create(session, name, address, phone, email)
        print(f"✅ Customer created: {customer}")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        session.close()

def delete_customer_interactive():
    try:
        id = int(input("Enter customer ID to delete: "))
    except ValueError:
        print("❌ Invalid ID. Must be a number.")
        return

    session = SessionLocal()
    try:
        customer = Customer.find_by_id(session, id)
        if not customer:
            print("Customer not found.")
            return
        customer.delete(session)
        print("🗑️ Customer deleted.")
    except Exception as e:
        print(f"❌ Error deleting customer: {e}")
    finally:
        session.close()

def list_customers_interactive():
    session = SessionLocal()
    try:
        customers = Customer.get_all(session)
        if customers:
            for c in customers:
                print(c)
        else:
            print("No customers found.")
    finally:
        session.close()

def find_customer_interactive():
    name = input("Enter name or partial name to search: ").strip()
    session = SessionLocal()
    try:
        results = Customer.find_by_name(session, name)
        if results:
            for c in results:
                print(c)
        else:
            print("No matching customers found.")
    finally:
        session.close()

def view_customer_related_objects():
    try:
        id = int(input("Enter customer ID to view orders: "))
    except ValueError:
        print("❌ Invalid ID.")
        return

    session = SessionLocal()
    try:
        customer = Customer.find_by_id(session, id)
        if not customer:
            print("Customer not found.")
            return

        orders = customer.orders  # Assumes relationship `orders` exists
        if orders:
            print(f"Orders for {customer.name}:")
            for order in orders:
                print(order)
        else:
            print("This customer has no orders.")
    except Exception as e:
        print(f"❌ Error fetching related objects: {e}")
    finally:
        session.close()
