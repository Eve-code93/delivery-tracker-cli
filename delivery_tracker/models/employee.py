from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)

    orders = relationship("Order", back_populates="employee", cascade="all, delete")

    # ORM Methods
    @classmethod
    def create(cls, session, name, role):
        employee = cls(name=name, role=role)
        session.add(employee)
        session.commit()
        return employee

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, emp_id):
        return session.query(cls).filter_by(id=emp_id).first()

    def delete(self, session):
        session.delete(self)
        session.commit()

    def __repr__(self):
        return f"<Employee id={self.id} name={self.name} role={self.role}>"
