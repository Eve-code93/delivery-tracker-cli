from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base

class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_info = Column(String)

    products = relationship("Product", back_populates="supplier", cascade="all, delete")

    @classmethod
    def create(cls, session, name, contact_info):
        supplier = cls(name=name, contact_info=contact_info)
        session.add(supplier)
        session.commit()
        return supplier

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, supplier_id):
        return session.query(cls).filter_by(id=supplier_id).first()

    @classmethod
    def find_by_name(cls, session, name):
        return session.query(cls).filter(cls.name.ilike(f"%{name}%")).all()

    def delete(self, session):
        session.delete(self)
        session.commit()

    def __repr__(self):
        return f"<Supplier id={self.id} name={self.name}>"
