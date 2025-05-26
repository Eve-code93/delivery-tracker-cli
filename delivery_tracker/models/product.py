from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    price = Column(Integer)
    in_stock = Column(Integer)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))

    supplier = relationship("Supplier", back_populates="products")
    order_details = relationship("OrderDetail", back_populates="product")
