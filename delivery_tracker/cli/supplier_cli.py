import click
from models.supplier import Supplier
from db.session import SessionLocal

@click.group()
def supplier_cli():
    """Commands to manage suppliers."""
    pass

# --- CLI Commands ---

@supplier_cli.command('create')
@click.option('--name', prompt=True, help="Supplier name")
@click.option('--contact-name', prompt=True, help="Contact person's name")
@click.option('--contact-email', prompt=True, help="Contact email")
@click.option('--contact-phone', prompt=True, help="Contact phone number")
def create_supplier(name, contact_name, contact_email, contact_phone):
    session = SessionLocal()
    try:
        supplier = Supplier.create(session, name, contact_name, contact_email, contact_phone)
        click.echo(f"✅ Supplier created: {supplier}")
    except Exception as e:
        click.echo(f"❌ Error creating supplier: {e}")
    finally:
        session.close()

@supplier_cli.command('list')
def list_suppliers():
    session = SessionLocal()
    try:
        suppliers = Supplier.get_all(session)
        if suppliers:
            click.echo("📦 Supplier List:")
            for s in suppliers:
                click.echo(s)
        else:
            click.echo("⚠️ No suppliers found.")
    finally:
        session.close()

@supplier_cli.command('delete')
@click.option('--id', prompt=True, type=int, help="ID of the supplier to delete")
def delete_supplier(id):
    session = SessionLocal()
    try:
        supplier = Supplier.find_by_id(session, id)
        if not supplier:
            click.echo("❌ Supplier not found.")
            return
        supplier.delete(session)
        click.echo("🗑️ Supplier deleted.")
    except Exception as e:
        click.echo(f"❌ Error deleting supplier: {e}")
    finally:
        session.close()

@supplier_cli.command('find')
@click.option('--name', prompt=True, help="Name or partial name of supplier")
def find_supplier(name):
    session = SessionLocal()
    try:
        results = Supplier.find_by_name(session, name)
        if results:
            for s in results:
                click.echo(s)
        else:
            click.echo("⚠️ No suppliers matched your search.")
    finally:
        session.close()

# --- Interactive Functions ---

def create_supplier_interactive():
    try:
        name = input("Enter supplier name: ")
        contact_name = input("Enter contact person’s name: ")
        contact_email = input("Enter contact email: ")
        contact_phone = input("Enter contact phone number: ")

        session = SessionLocal()
        supplier = Supplier.create(session, name, contact_name, contact_email, contact_phone)
        print(f"✅ Supplier created: {supplier}")
    except Exception as e:
        print(f"❌ Error creating supplier: {e}")
    finally:
        session.close()

def list_suppliers_interactive():
    session = SessionLocal()
    try:
        suppliers = Supplier.get_all(session)
        if suppliers:
            print("📦 Supplier List:")
            for s in suppliers:
                print(s)
        else:
            print("⚠️ No suppliers found.")
    finally:
        session.close()

def delete_supplier_interactive():
    try:
        id = int(input("Enter supplier ID to delete: "))
    except ValueError:
        print("❌ Invalid ID.")
        return

    session = SessionLocal()
    try:
        supplier = Supplier.find_by_id(session, id)
        if not supplier:
            print("❌ Supplier not found.")
            return
        supplier.delete(session)
        print("🗑️ Supplier deleted.")
    except Exception as e:
        print(f"❌ Error deleting supplier: {e}")
    finally:
        session.close()

def find_supplier_interactive():
    name = input("Enter supplier name or partial name to search: ")
    session = SessionLocal()
    try:
        results = Supplier.find_by_name(session, name)
        if results:
            for s in results:
                print(s)
        else:
            print("⚠️ No suppliers matched your search.")
    finally:
        session.close()
