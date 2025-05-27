import click
from models.base import Base
from models.product import Product
from models.supplier import Supplier
from db.session import SessionLocal

session = SessionLocal()

@click.group()
def product_cli():
    """Commands to manage products."""
    pass

@product_cli.command()
def list():
    """Display all products."""
    products = Product.get_all(session)
    if not products:
        click.echo("No products found.")
        return
    for p in products:
        click.echo(f"ID: {p.id} | Name: {p.name} | Price: {p.price} | Supplier ID: {p.supplier_id}")

@product_cli.command()
def create():
    """Create a new product."""
    try:
        name = click.prompt("Product name", type=str)
        price = click.prompt("Price", type=float)
        
        # List suppliers to choose from
        suppliers = Supplier.get_all(session)
        if not suppliers:
            click.echo("No suppliers found. Please create a supplier first.")
            return
        click.echo("Available suppliers:")
        for s in suppliers:
            click.echo(f"{s.id}: {s.name}")
        supplier_id = click.prompt("Supplier ID", type=int)
        
        supplier = Supplier.find_by_id(session, supplier_id)
        if not supplier:
            click.echo("Supplier not found.")
            return
        
        product = Product.create(session, name, price, supplier_id)
        click.echo(f"Created product: {product}")
    except Exception as e:
        click.echo(f"Error creating product: {e}")

@product_cli.command()
@click.argument("product_id", type=int)
def delete(product_id):
    """Delete a product by ID."""
    product = Product.find_by_id(session, product_id)
    if not product:
        click.echo("Product not found.")
        return
    
    confirm = click.confirm(f"Are you sure you want to delete product '{product.name}'?")
    if confirm:
        try:
            product.delete(session)
            click.echo("Product deleted.")
        except Exception as e:
            click.echo(f"Error deleting product: {e}")

@product_cli.command()
@click.argument("product_id", type=int)
def view_supplier(product_id):
    """View the supplier details of a product."""
    product = Product.find_by_id(session, product_id)
    if not product:
        click.echo("Product not found.")
        return
    
    supplier = product.supplier
    if supplier:
        click.echo(f"Supplier ID: {supplier.id}")
        click.echo(f"Supplier Name: {supplier.name}")
    else:
        click.echo("This product has no associated supplier.")

@product_cli.command()
@click.option('--name', help="Search products by name (partial match).")
@click.option('--id', 'prod_id', type=int, help="Search product by ID.")
def find(name, prod_id):
    """Find products by name or ID."""
    if name:
        results = Product.find_by_name(session, name)
        if results:
            for p in results:
                click.echo(f"ID: {p.id} | Name: {p.name} | Price: {p.price} | Supplier ID: {p.supplier_id}")
        else:
            click.echo("No products found with that name.")
    elif prod_id is not None:
        p = Product.find_by_id(session, prod_id)
        if p:
            click.echo(f"ID: {p.id} | Name: {p.name} | Price: {p.price} | Supplier ID: {p.supplier_id}")
        else:
            click.echo("Product not found.")
    else:
        click.echo("Please provide --name or --id option.")

if __name__ == "__main__":
    product_cli()
