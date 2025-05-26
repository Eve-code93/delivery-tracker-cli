from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class OrderDetail(Base):
    __tablename__ = 'order_details'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))

    order = relationship("Order", back_populates="order_details")
    product = relationship("Product", back_populates="order_details")
