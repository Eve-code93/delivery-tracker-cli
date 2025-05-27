from sqlalchemy import Column, Integer, String
from models.base import Base

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    phone_number = Column(String)
    email = Column(String)
