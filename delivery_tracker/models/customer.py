from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    orders = relationship("Order", back_populates="customer", cascade="all, delete")

    @classmethod
    def create(cls, session, name, email):
        customer = cls(name=name, email=email)
        session.add(customer)
        session.commit()
        return customer

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, cust_id):
        return session.query(cls).filter_by(id=cust_id).first()

    @classmethod
    def find_by_email(cls, session, email):
        return session.query(cls).filter_by(email=email).first()

    def delete(self, session):
        session.delete(self)
        session.commit()

    def __repr__(self):
        return f"<Customer id={self.id} name={self.name} email={self.email}>"
