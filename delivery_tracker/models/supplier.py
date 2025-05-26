from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)

    products = relationship("Product", back_populates="supplier")
