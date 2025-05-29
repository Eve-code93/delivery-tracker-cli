from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    price = Column(Integer, nullable=False)
    in_stock = Column(Integer, nullable=False)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'), nullable=False)

    supplier = relationship("Supplier", back_populates="products")
    order_details = relationship("OrderDetail", back_populates="product", cascade="all, delete-orphan")

    @classmethod
    def create(cls, session, name, type, price, in_stock, supplier_id):
        product = cls(name=name, type=type, price=price, in_stock=in_stock, supplier_id=supplier_id)
        session.add(product)
        session.commit()
        return product

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, prod_id):
        return session.query(cls).filter_by(id=prod_id).first()

    def delete(self, session):
        session.delete(self)
        session.commit()

    def __repr__(self):
        return (f"<Product id={self.id} name={self.name} "
                f"price={self.price} in_stock={self.in_stock} supplier_id={self.supplier_id}>")
