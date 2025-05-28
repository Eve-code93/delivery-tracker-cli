import click
from models.product import Product
from db.session import SessionLocal

@click.group()
def product_cli():
    """Commands to manage products."""
    pass

@product_cli.command('create')
@click.option('--name', prompt=True)
@click.option('--type', prompt='Type (e.g. furniture, accessory)')
@click.option('--price', prompt=True, type=int)
@click.option('--in-stock', prompt='Quantity in stock', type=int)
@click.option('--supplier-id', prompt=True, type=int)
def create_product(name, type, price, in_stock, supplier_id):
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
            for p in products:
                click.echo(p)
        else:
            click.echo("No products found.")
    finally:
        session.close()

@product_cli.command('delete')
@click.option('--id', prompt=True, type=int)
def delete_product(id):
    session = SessionLocal()
    try:
        product = Product.find_by_id(session, id)
        if not product:
            click.echo("Product not found.")
            return
        product.delete(session)
        click.echo("🗑️ Product deleted.")
    except Exception as e:
        click.echo(f"Error deleting product: {e}")
    finally:
        session.close()
