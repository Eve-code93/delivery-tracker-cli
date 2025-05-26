from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from . import Base

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    role = Column(String)
    date_employed = Column(Date)

    orders = relationship("Order", back_populates="employee")
