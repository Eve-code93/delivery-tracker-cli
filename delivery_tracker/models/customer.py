from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String)
    phone_number = Column(String)
    email = Column(String, nullable=False)

    orders = relationship("Order", back_populates="customer", cascade="all, delete-orphan")

    @classmethod
    def create(cls, session, name, address, phone_number, email):
        customer = cls(name=name, address=address, phone_number=phone_number, email=email)
        session.add(customer)
        session.commit()
        return customer

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, customer_id):
        return session.query(cls).filter_by(id=customer_id).first()

    @classmethod
    def find_by_name(cls, session, name):
        return session.query(cls).filter(cls.name.ilike(f"%{name}%")).all()

    def delete(self, session):
        session.delete(self)
        session.commit()

    def __repr__(self):
        return (f"<Customer id={self.id} name={self.name} "
                f"address={self.address} phone={self.phone_number} email={self.email}>")
