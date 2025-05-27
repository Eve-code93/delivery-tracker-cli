from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    employee_id = Column(Integer, ForeignKey('employees.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))

    employee = relationship("Employee", back_populates="orders")
    customer = relationship("Customer", back_populates="orders")

    # One-to-many relationship with OrderDetail
    order_details = relationship("OrderDetail", back_populates="order", cascade="all, delete-orphan")

    @classmethod
    def create(cls, session, description, employee_id, customer_id):
        order = cls(description=description, employee_id=employee_id, customer_id=customer_id)
        session.add(order)
        session.commit()
        return order

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, order_id):
        return session.query(cls).filter_by(id=order_id).first()

    def delete(self, session):
        session.delete(self)
        session.commit()

    def __repr__(self):
        return f"<Order id={self.id} description={self.description}>"
