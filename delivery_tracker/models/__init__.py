# delivery_tracker/models/__init__.py
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Import all model files here, but only AFTER Base is defined
from .customer import Customer
from .employee import Employee
from .product import Product
from .order import Order
from .order_detail import OrderDetail
from .supplier import Supplier
