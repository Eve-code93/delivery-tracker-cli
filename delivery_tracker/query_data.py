from delivery_tracker.models import Employee  # adjust import path
from db import SessionLocal

def get_employees():
    session = SessionLocal()
    try:
        employees = session.query(Employee).all()
        for emp in employees:
            print(f"Employee ID: {emp.id}, Name: {emp.name}")
    finally:
        session.close()

if __name__ == "__main__":
    get_employees()
