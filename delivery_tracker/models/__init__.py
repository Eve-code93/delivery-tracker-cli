from sqlalchemy.orm import declarative_base

Base = declarative_base()
from .customer import Customer
from.employee import Employee
from .order import Order
from .product import Product
from .order_detail import OrderDetail
from .order import Order    
from .supplier import Supplier