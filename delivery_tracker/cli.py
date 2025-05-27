import click
from db import SessionLocal
from models.employee import Employee
from models.customer import Customer
from models.product import Product
from models.order import Order
from models.order_detail import OrderDetail

session = SessionLocal()

@click.group()
def cli():
    """Delivery Tracker CLI Application."""
    pass

### EMPLOYEE COMMANDS ###
@cli.group()
def employee():
    """Commands to manage employees."""
    pass

@employee.command()
@click.argument('name')
def create(name):
    """Create a new employee."""
    new_employee = Employee(name=name)
    session.add(new_employee)
    session.commit()
    click.echo(f"Employee created with id: {new_employee.id}")

@employee.command()
def list():
    """List all employees."""
    employees = session.query(Employee).all()
    for e in employees:
        click.echo(f"{e.id}: {e.name}")

@employee.command()
@click.argument('employee_id', type=int)
def delete(employee_id):
    """Delete an employee by ID."""
    employee = session.query(Employee).get(employee_id)
    if employee:
        session.delete(employee)
        session.commit()
        click.echo(f"Deleted employee with id {employee_id}")
    else:
        click.echo("Employee not found.")

@employee.command()
@click.argument('employee_id', type=int)
def find(employee_id):
    """Find an employee by ID."""
    employee = session.query(Employee).get(employee_id)
    if employee:
        click.echo(f"Employee {employee.id}: {employee.name}")
    else:
        click.echo("Employee not found.")

@employee.command()
@click.argument('employee_id', type=int)
def orders(employee_id):
    """List orders handled by an employee."""
    employee = session.query(Employee).get(employee_id)
    if employee:
        if employee.orders:
            for order in employee.orders:
                click.echo(f"Order {order.id}: {order.description}")
        else:
            click.echo("No orders found for this employee.")
    else:
        click.echo("Employee not found.")

### CUSTOMER COMMANDS ###
@cli.group()
def customer():
    """Commands to manage customers."""
    pass

@customer.command()
@click.argument('name')
def create(name):
    """Create a new customer."""
    new_customer = Customer(name=name)
    session.add(new_customer)
    session.commit()
    click.echo(f"Customer created with id: {new_customer.id}")

@customer.command()
def list():
    """List all customers."""
    customers = session.query(Customer).all()
    for c in customers:
        click.echo(f"{c.id}: {c.name}")

@customer.command()
@click.argument('customer_id', type=int)
def delete(customer_id):
    """Delete a customer by ID."""
    customer = session.query(Customer).get(customer_id)
    if customer:
        session.delete(customer)
        session.commit()
        click.echo(f"Deleted customer with id {customer_id}")
    else:
        click.echo("Customer not found.")

@customer.command()
@click.argument('customer_id', type=int)
def find(customer_id):
    """Find a customer by ID."""
    customer = session.query(Customer).get(customer_id)
    if customer:
        click.echo(f"Customer {customer.id}: {customer.name}")
    else:
        click.echo("Customer not found.")

@customer.command()
@click.argument('customer_id', type=int)
def orders(customer_id):
    """List orders placed by a customer."""
    customer = session.query(Customer).get(customer_id)
    if customer:
        if customer.orders:
            for order in customer.orders:
                click.echo(f"Order {order.id}: {order.description}")
        else:
            click.echo("No orders found for this customer.")
    else:
        click.echo("Customer not found.")

### PRODUCT COMMANDS ###
@cli.group()
def product():
    """Commands to manage products."""
    pass

@product.command()
@click.argument('name')
def create(name):
    """Create a new product."""
    new_product = Product(name=name)
    session.add(new_product)
    session.commit()
    click.echo(f"Product created with id: {new_product.id}")

@product.command()
def list():
    """List all products."""
    products = session.query(Product).all()
    for p in products:
        click.echo(f"{p.id}: {p.name}")

@product.command()
@click.argument('product_id', type=int)
def delete(product_id):
    """Delete a product by ID."""
    product = session.query(Product).get(product_id)
    if product:
        session.delete(product)
        session.commit()
        click.echo(f"Deleted product with id {product_id}")
    else:
        click.echo("Product not found.")

@product.command()
@click.argument('product_id', type=int)
def find(product_id):
    """Find a product by ID."""
    product = session.query(Product).get(product_id)
    if product:
        click.echo(f"Product {product.id}: {product.name}")
    else:
        click.echo("Product not found.")

@product.command()
@click.argument('product_id', type=int)
def order_details(product_id):
    """List order details related to a product."""
    product = session.query(Product).get(product_id)
    if product:
        if product.order_details:
            for detail in product.order_details:
                click.echo(f"OrderDetail {detail.id}: Order {detail.order_id}, Qty {detail.quantity}, Price {detail.price}")
        else:
            click.echo("No order details found for this product.")
    else:
        click.echo("Product not found.")

### ORDER COMMANDS ###
@cli.group()
def order():
    """Commands to manage orders."""
    pass

@order.command()
@click.argument('description')
@click.argument('employee_id', type=int)
@click.argument('customer_id', type=int)
def create(description, employee_id, customer_id):
    """Create a new order."""
    new_order = Order(description=description, employee_id=employee_id, customer_id=customer_id)
    session.add(new_order)
    session.commit()
    click.echo(f"Order created with id: {new_order.id}")

@order.command()
def list():
    """List all orders."""
    orders = session.query(Order).all()
    for o in orders:
        click.echo(f"{o.id}: {o.description} (Employee: {o.employee_id}, Customer: {o.customer_id})")

@order.command()
@click.argument('order_id', type=int)
def delete(order_id):
    """Delete an order by ID."""
    order = session.query(Order).get(order_id)
    if order:
        session.delete(order)
        session.commit()
        click.echo(f"Deleted order with id {order_id}")
    else:
        click.echo("Order not found.")

@order.command()
@click.argument('order_id', type=int)
def find(order_id):
    """Find an order by ID."""
    order = session.query(Order).get(order_id)
    if order:
        click.echo(f"Order {order.id}: {order.description}, Employee {order.employee_id}, Customer {order.customer_id}")
    else:
        click.echo("Order not found.")

@order.command()
@click.argument('order_id', type=int)
def details(order_id):
    """List order details for an order."""
    order = session.query(Order).get(order_id)
    if order:
        if order.order_details:
            for detail in order.order_details:
                click.echo(f"OrderDetail {detail.id}: Product {detail.product_id}, Qty {detail.quantity}, Price {detail.price}")
        else:
            click.echo("No order details found for this order.")
    else:
        click.echo("Order not found.")

### ORDER_DETAIL COMMANDS ###
@cli.group()
def order_detail():
    """Commands to manage order details."""
    pass

@order_detail.command()
@click.argument('order_id', type=int)
@click.argument('product_id', type=int)
@click.argument('quantity', type=int)
@click.argument('price', type=float)
def create(order_id, product_id, quantity, price):
    """Create a new order detail."""
    new_detail = OrderDetail(order_id=order_id, product_id=product_id, quantity=quantity, price=price)
    session.add(new_detail)
    session.commit()
    click.echo(f"OrderDetail created with id: {new_detail.id}")

@order_detail.command()
def list():
    """List all order details."""
    details = session.query(OrderDetail).all()
    for d in details:
        click.echo(f"{d.id}: Order {d.order_id}, Product {d.product_id}, Qty {d.quantity}, Price {d.price}")

@order_detail.command()
@click.argument('detail_id', type=int)
def delete(detail_id):
    """Delete an order detail by ID."""
    detail = session.query(OrderDetail).get(detail_id)
    if detail:
        session.delete(detail)
        session.commit()
        click.echo(f"Deleted order detail with id {detail_id}")
    else:
        click.echo("Order detail not found.")

@order_detail.command()
@click.argument('detail_id', type=int)
def find(detail_id):
    """Find an order detail by ID."""
    detail = session.query(OrderDetail).get(detail_id)
    if detail:
        click.echo(f"OrderDetail {detail.id}: Order {detail.order_id}, Product {detail.product_id}, Qty {detail.quantity}, Price {detail.price}")
    else:
        click.echo("Order detail not found.")

if __name__ == '__main__':
    cli()
