
import click
from datetime import datetime
from models.employee import Employee
from db.session import SessionLocal

@click.group()
def employee_cli():
    """Commands to manage employees."""
    pass

# --- CLI commands ---

@employee_cli.command('create')
@click.option('--name', prompt=True, help='Employee name')
@click.option('--age', prompt=True, type=int, help='Employee age')
@click.option('--gender', prompt=True, type=click.Choice(['Male', 'Female', 'Other'], case_sensitive=False))
@click.option('--role', prompt=True, help='Employee role')
@click.option('--date-employed', prompt='Date employed (YYYY-MM-DD)', help='Date the employee was hired')
def create_employee(name, age, gender, role, date_employed):
    session = SessionLocal()
    try:
        date_employed_obj = datetime.strptime(date_employed, "%Y-%m-%d").date()
        employee = Employee.create(
            session=session,
            name=name,
            age=age,
            gender=gender,
            role=role,
            date_employed=date_employed_obj
        )
        click.echo(f"✅ Employee created: {employee}")
    except Exception as e:
        click.echo(f"❌ Error creating employee: {e}")
    finally:
        session.close()

@employee_cli.command('list')
def list_employees():
    session = SessionLocal()
    try:
        employees = Employee.get_all(session)
        if employees:
            click.echo("📋 All Employees:")
            for e in employees:
                click.echo(e)
        else:
            click.echo("⚠️ No employees found.")
    finally:
        session.close()

@employee_cli.command('delete')
@click.option('--id', prompt=True, type=int, help='Employee ID to delete')
def delete_employee(id):
    session = SessionLocal()
    try:
        employee = Employee.find_by_id(session, id)
        if not employee:
            click.echo("❌ Employee not found.")
            return
        employee.delete(session)
        click.echo("🗑️ Employee deleted.")
    except Exception as e:
        click.echo(f"❌ Error deleting employee: {e}")
    finally:
        session.close()

@employee_cli.command('find')
@click.option('--name', prompt=True, help='Name or partial name to search')
def find_employee(name):
    session = SessionLocal()
    try:
        results = Employee.find_by_name(session, name)
        if results:
            click.echo("🔍 Search Results:")
            for e in results:
                click.echo(e)
        else:
            click.echo("⚠️ No employees matched your search.")
    finally:
        session.close()

# --- Interactive functions for custom CLI ---

def create_employee_interactive():
    name = input("Enter employee name: ").strip()
    try:
        age = int(input("Enter age: "))
    except ValueError:
        print("❌ Invalid age.")
        return

    gender = input("Enter gender (Male/Female/Other): ").strip().capitalize()
    if gender not in ['Male', 'Female', 'Other']:
        print("❌ Invalid gender.")
        return

    role = input("Enter role: ").strip()
    date_str = input("Enter date employed (YYYY-MM-DD): ").strip()

    try:
        date_employed = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("❌ Invalid date format.")
        return

    session = SessionLocal()
    try:
        employee = Employee.create(
            session=session,
            name=name,
            age=age,
            gender=gender,
            role=role,
            date_employed=date_employed
        )
        print(f"✅ Employee created: {employee}")
    except Exception as e:
        print(f"❌ Error creating employee: {e}")
    finally:
        session.close()

def list_employees_interactive():
    session = SessionLocal()
    try:
        employees = Employee.get_all(session)
        if employees:
            print("📋 Employees:")
            for e in employees:
                print(e)
        else:
            print("⚠️ No employees found.")
    finally:
        session.close()

def delete_employee_interactive():
    try:
        id = int(input("Enter employee ID to delete: "))
    except ValueError:
        print("❌ Invalid ID.")
        return

    session = SessionLocal()
    try:
        employee = Employee.find_by_id(session, id)
        if not employee:
            print("❌ Employee not found.")
            return
        employee.delete(session)
        print("🗑️ Employee deleted.")
    except Exception as e:
        print(f"❌ Error deleting employee: {e}")
    finally:
        session.close()

def find_employee_interactive():
    name = input("Enter name or partial name to search: ").strip()
    session = SessionLocal()
    try:
        results = Employee.find_by_name(session, name)
        if results:
            print("🔍 Search Results:")
            for e in results:
                print(e)
        else:
            print("⚠️ No employees matched your search.")
    finally:
        session.close()
