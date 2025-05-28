from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from models.base import Base

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    total_price = Column(Integer, nullable=False)
    time = Column(DateTime, default=datetime.utcnow)
    employee_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)

    employee = relationship("Employee", back_populates="orders")
    customer = relationship("Customer", back_populates="orders")
    order_details = relationship("OrderDetail", back_populates="order", cascade="all, delete-orphan")

    # ORM methods
    @classmethod
    def create(cls, session, total_price, employee_id, customer_id, time=None):
        time = time or datetime.utcnow()
        order = cls(
            total_price=total_price,
            time=time,
            employee_id=employee_id,
            customer_id=customer_id
        )
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
        return (f"<Order id={self.id} total_price={self.total_price} "
                f"time={self.time} customer_id={self.customer_id} "
                f"employee_id={self.employee_id}>")
