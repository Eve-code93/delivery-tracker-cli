import click
from models.customer import Customer
from db.session import SessionLocal

@click.group()
def customer_cli():
    """Commands to manage customers."""
    pass

@customer_cli.command('create')
@click.option('--name', prompt=True, help='Customer name')
@click.option('--email', prompt=True, help='Customer email')
def create_customer(name, email):
    session = SessionLocal()
    try:
        customer = Customer.create(session, name, email)
        click.echo(f"Customer created: {customer}")
    except Exception as e:
        click.echo(f"Error creating customer: {e}")
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
@click.option('--id', prompt=True, type=int, help='Customer ID to delete')
def delete_customer(id):
    session = SessionLocal()
    try:
        customer = Customer.find_by_id(session, id)
        if not customer:
            click.echo("Customer not found.")
            return
        customer.delete(session)
        click.echo("Customer deleted.")
    except Exception as e:
        click.echo(f"Error deleting customer: {e}")
    finally:
        session.close()

@customer_cli.command('find')
@click.option('--name', prompt=True, help='Name or partial name to search')
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



