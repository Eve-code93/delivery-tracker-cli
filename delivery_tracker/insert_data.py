from models.employee import Employee  # adjust import path
from db import SessionLocal

def create_employee(name: str):
    session = SessionLocal()
    try:
        new_employee = Employee(name=name)
        session.add(new_employee)
        session.commit()
        print(f"Created employee with id: {new_employee.id}")
    except Exception as e:
        session.rollback()
        print("Failed to create employee:", e)
    finally:
        session.close()

if __name__ == "__main__":
    create_employee("Mwangi John")  # Example employee name
# This script creates a new employee in the database.