from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class OrderDetail(Base):
    __tablename__ = 'order_details'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)

    order = relationship("Order", back_populates="order_details")
    product = relationship("Product", back_populates="order_details")

    # ORM Methods
    @classmethod
    def create(cls, session, order_id, product_id):
        detail = cls(order_id=order_id, product_id=product_id)
        session.add(detail)
        session.commit()
        return detail

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
        return f"<OrderDetail id={self.id} order_id={self.order_id} product_id={self.product_id}>"
