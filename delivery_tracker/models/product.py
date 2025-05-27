from sqlalchemy import Column, Integer, String, ForeignKey
from models.base import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    price = Column(Integer)
    in_stock = Column(Integer)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))
