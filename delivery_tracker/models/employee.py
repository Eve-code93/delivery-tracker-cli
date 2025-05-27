from sqlalchemy import Column, Integer, String, Date
from models.base import Base

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    role = Column(String)
    date_employed = Column(Date)
