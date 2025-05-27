import click
from models.employee import Employee
from db.session import SessionLocal
@click.group()
def employee_cli():
    """Commands to manage employees."""
    pass

@employee_cli.command('create')
@click.option('--name', prompt=True, help='Employee name')
def create_employee(name):
    session = SessionLocal()
    try:
        employee = Employee.create(session, name)
        click.echo(f"Employee created: {employee}")
    except Exception as e:
        click.echo(f"Error creating employee: {e}")
    finally:
        session.close()

@employee_cli.command('list')
def list_employees():
    session = SessionLocal()
    try:
        employees = Employee.get_all(session)
        if employees:
            for e in employees:
                click.echo(e)
        else:
            click.echo("No employees found.")
    finally:
        session.close()

@employee_cli.command('delete')
@click.option('--id', prompt=True, type=int, help='Employee ID to delete')
def delete_employee(id):
    session = SessionLocal()
    try:
        employee = Employee.find_by_id(session, id)
        if not employee:
            click.echo("Employee not found.")
            return
        employee.delete(session)
        click.echo("Employee deleted.")
    except Exception as e:
        click.echo(f"Error deleting employee: {e}")
    finally:
        session.close()

@employee_cli.command('find')
@click.option('--name', prompt=True, help='Name or partial name to search')
def find_employee(name):
    session = SessionLocal()
    try:
        results = Employee.find_by_name(session, name)
        if results:
            for e in results:
                click.echo(e)
        else:
            click.echo("No employees matched your search.")
    finally:
        session.close()

# Add related objects commands as needed...
