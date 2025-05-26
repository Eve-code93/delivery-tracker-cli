from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    total_price = Column(Integer)
    time = Column(DateTime)
    employee_id = Column(Integer, ForeignKey('employees.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))

    employee = relationship("Employee", back_populates="orders")
    customer = relationship("Customer", back_populates="orders")
    order_details = relationship("OrderDetail", back_populates="order")
