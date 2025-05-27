from sqlalchemy import Column, Integer, ForeignKey, DateTime
from models.base import Base

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    total_price = Column(Integer)
    time = Column(DateTime)
    employee_id = Column(Integer, ForeignKey('employees.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
