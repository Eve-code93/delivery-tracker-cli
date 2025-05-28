from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base

class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_name = Column(String)
    contact_email = Column(String)
    contact_phone = Column(String)

    products = relationship("Product", back_populates="supplier", cascade="all, delete-orphan")

    @classmethod
    def create(cls, session, name, contact_name, contact_email, contact_phone):
        supplier = cls(
            name=name,
            contact_name=contact_name,
            contact_email=contact_email,
            contact_phone=contact_phone
        )
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
        return (
            f"<Supplier id={self.id} name={self.name} "
            f"contact_name={self.contact_name} email={self.contact_email} phone={self.contact_phone}>"
        )
