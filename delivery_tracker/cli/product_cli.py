import click
from models.product import Product
from db.session import SessionLocal

@click.group()
def product_cli():
    """Commands to manage products."""
    pass

# --- CLI Commands ---

@product_cli.command('create')
@click.option('--name', prompt=True)
@click.option('--price', prompt=True, )
@click.option('--in-stock', prompt='Quantity in stock', )
@click.option('--supplier-id', prompt=True, )
def create_product(name, price, in_stock, supplier_id):
    session = SessionLocal()
    try:
        product = Product.create(session, name, type, price, in_stock, supplier_id)
        click.echo(f"✅ Product created: {product}")
    except Exception as e:
        click.echo(f"❌ Error creating product: {e}")
    finally:
        session.close()

@product_cli.command('list')
def list_products():
    session = SessionLocal()
    try:
        products = Product.get_all(session)
        if products:
            click.echo("🛒 Product List:")
            for p in products:
                click.echo(p)
        else:
            click.echo("⚠️ No products found.")
    finally:
        session.close()

@product_cli.command('delete')
@click.option('--id', prompt=True,)
def delete_product(id):
    session = SessionLocal()
    try:
        product = Product.find_by_id(session, id)
        if not product:
            click.echo("❌ Product not found.")
            return
        product.delete(session)
        click.echo("🗑️ Product deleted.")
    except Exception as e:
        click.echo(f"❌ Error deleting product: {e}")
    finally:
        session.close()

# --- Interactive Functions ---

def create_product_interactive():
    try:
        name = input("Enter product name: ")
        type_ = input("Enter product type (e.g. furniture, accessory): ")
        price = int(input("Enter price: "))
        in_stock = int(input("Enter quantity in stock: "))
        supplier_id = int(input("Enter supplier ID: "))

        session = SessionLocal()
        product = Product.create(session, name, type_, price, in_stock, supplier_id)
        print(f"✅ Product created: {product}")
    except ValueError:
        print("❌ Invalid input. Please use correct data types.")
    except Exception as e:
        print(f"❌ Error creating product: {e}")
    finally:
        session.close()

def list_products_interactive():
    session = SessionLocal()
    try:
        products = Product.get_all(session)
        if products:
            print("🛒 Product List:")
            for p in products:
                print(p)
        else:
            print("⚠️ No products found.")
    finally:
        session.close()

def delete_product_interactive():
    try:
        id = int(input("Enter product ID to delete: "))
    except ValueError:
        print("❌ Invalid ID.")
        return

    session = SessionLocal()
    try:
        product = Product.find_by_id(session, id)
        if not product:
            print("❌ Product not found.")
            return
        product.delete(session)
        print("🗑️ Product deleted.")
    except Exception as e:
        print(f"❌ Error deleting product: {e}")
    finally:
        session.close()
