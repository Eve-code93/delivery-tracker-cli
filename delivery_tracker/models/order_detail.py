from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from models.base import Base

class OrderDetail(Base):
    __tablename__ = 'order_details'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)

    order = relationship("Order", back_populates="order_details")
    product = relationship("Product", back_populates="order_details")

    @classmethod
    def create(cls, session, order_id, product_id, quantity, price):
        order_detail = cls(order_id=order_id, product_id=product_id, quantity=quantity, price=price)
        session.add(order_detail)
        session.commit()
        return order_detail

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, detail_id):
        return session.query(cls).filter_by(id=detail_id).first()

    def delete(self, session):
        session.delete(self)
        session.commit()

    def __repr__(self):
        return f"<OrderDetail id={self.id} order_id={self.order_id} product_id={self.product_id} quantity={self.quantity} price={self.price}>"
