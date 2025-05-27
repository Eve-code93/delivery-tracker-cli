from db import SessionLocal
from models.employee import Employee
from models.customer import Customer
from models.supplier import Supplier
from models.product import Product
from models.order import Order
from models.order_detail import OrderDetail
import datetime


def insert_sample_data():
    with SessionLocal() as session:
        try:
            # Employees
            emp1 = Employee(name="John Mwangi", role="driver")
            emp2 = Employee(name="Alice Kimani", role="dispatcher")
            session.add_all([emp1, emp2])

            # Customers
            cust1 = Customer(name="Jane Doe", email="jane@example.com")
            cust2 = Customer(name="Peter Njuguna", email="peter@example.com")
            session.add_all([cust1, cust2])

            # Suppliers
            sup1 = Supplier(name="Jumia Kenya", contact_info="info@jumia.co.ke")
            sup2 = Supplier(name="Safaricom Ltd", contact_info="contact@safaricom.co.ke")
            session.add_all([sup1, sup2])

            # Products
            prod1 = Product(name="Smartphone", price=15000.0, supplier_id=1)
            prod2 = Product(name="Router", price=7000.0, supplier_id=2)
            session.add_all([prod1, prod2])

            # Orders
            order1 = Order(customer_id=1, description="Order for delivery")
            order2 = Order(customer_id=2, description="Bulk order for office")
            session.add_all([order1, order2])

            # Order Details
            od1 = OrderDetail(order_id=1, product_id=1, quantity=2, price=15000.0)
            od2 = OrderDetail(order_id=2, product_id=2, quantity=3, price=7000.0)
            session.add_all([od1, od2])

            session.commit()
            print("Sample data inserted successfully.")
        except Exception as e:
            session.rollback()
            print("Failed to insert sample data:", e)


if __name__ == "__main__":
    insert_sample_data()
