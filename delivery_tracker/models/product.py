from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))

    supplier = relationship("Supplier", back_populates="products")
    order_details = relationship("OrderDetail", back_populates="product", cascade="all, delete")

    @classmethod
    def create(cls, session, name, price, supplier_id):
        product = cls(name=name, price=price, supplier_id=supplier_id)
        session.add(product)
        session.commit()
        return product

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, product_id):
        return session.query(cls).filter_by(id=product_id).first()

    @classmethod
    def find_by_name(cls, session, name):
        return session.query(cls).filter(cls.name.ilike(f"%{name}%")).all()

    def delete(self, session):
        session.delete(self)
        session.commit()

    def __repr__(self):
        return f"<Product id={self.id} name={self.name} price={self.price}>"
# Ensure that the Supplier model is imported to establish the relationship