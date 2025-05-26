from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    phone_number = Column(String)
    email = Column(String)

    orders = relationship("Order", back_populates="customer")
