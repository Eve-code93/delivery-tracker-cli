import sys
import os
import logging

# Set up paths and silence noisy SQL logs
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)


try:
    from db.session import engine
    from models import Base 
    Base.metadata.create_all(bind=engine)
    print("✅ Database and tables are ready.")
except Exception as e:
    print(f"❌ Error setting up the database: {e}")
    sys.exit(1)

# Import CLI interaction modules
try:
    from cli.customer_cli import (
        create_customer_interactive, list_customers_interactive,
        delete_customer_interactive,
        find_customer_interactive, view_customer_related_objects
    )
    from cli.employee_cli import (
        create_employee_interactive, list_employees_interactive,
        delete_employee_interactive, find_employee_interactive
    )
    from cli.product_cli import (
        create_product_interactive, list_products_interactive,
        delete_product_interactive, 
    )
    from cli.order_cli import (
        create_order_interactive, list_orders_interactive,
        delete_order_interactive, 
    )
    from cli.order_detail_cli import (
        create_order_detail_interactive, list_order_details_interactive,
         delete_order_detail_interactive, 
    )
    from cli.supplier_cli import (
        create_supplier_interactive, list_suppliers_interactive,
        delete_supplier_interactive, find_supplier_interactive
    )
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("➡️ Make sure you run this script from the project root and your `cli/` folder exists.")
    sys.exit(1)

# ---------- SUB-MENU DEFINITIONS ----------

def customer_menu():
    while True:
        print("\n📋 CUSTOMER MENU")
        print("1. Create")
        print("2. List")
        print("3. Find")
        print("4. Delete")
        print("5. View Related Orders")
        print("6. Back")
        choice = input("Choose: ").strip()
        match choice:
            case '1': create_customer_interactive()
            case '2': list_customers_interactive()
            case '3': find_customer_interactive()
            case '4': delete_customer_interactive()
            case '5': view_customer_related_objects()
            case '6': break
            case _: print("❌ Invalid choice.")

def employee_menu():
    while True:
        print("\n👤 EMPLOYEE MENU")
        print("1. Create")
        print("2. List")
        print("3. Find")
        print("4. Delete")
        print("5. Back")
        choice = input("Choose: ").strip()
        match choice:
            case '1': create_employee_interactive()
            case '2': list_employees_interactive()
            case '3': find_employee_interactive()
            case '4': delete_employee_interactive()
            case '5': break
            case _: print("❌ Invalid choice.")

def product_menu():
    while True:
        print("\n📦 PRODUCT MENU")
        print("1. Create")
        print("2. List")
    
        print("4. Delete")
        print("5. Back")
        choice = input("Choose: ").strip()
        match choice:
            case '1': create_product_interactive()
            case '2': list_products_interactive()
            case '4': delete_product_interactive()
            case '5': break
            case _: print("❌ Invalid choice.")

def order_menu():
    while True:
        print("\n🧾 ORDER MENU")
        print("1. Create")
        print("2. List")
        print("3. Find")
        print("4. Delete")
        print("5. Back")
        choice = input("Choose: ").strip()
        match choice:
            case '1': create_order_interactive()
            case '2': list_orders_interactive()
            case '3': find_order_interactive()
            case '4': delete_order_interactive()
            case '5': break
            case _: print("❌ Invalid choice.")

def order_detail_menu():
    while True:
        print("\n📄 ORDER DETAIL MENU")
        print("1. Create")
        print("2. List")
        print("3. Find")
        print("4. Delete")
        print("5. Back")
        choice = input("Choose: ").strip()
        match choice:
            case '1': create_order_detail_interactive()
            case '2': list_order_details_interactive()
            case '3': find_order_detail_interactive()
            case '4': delete_order_detail_interactive()
            case '5': break
            case _: print("❌ Invalid choice.")

def supplier_menu():
    while True:
        print("\n🏭 SUPPLIER MENU")
        print("1. Create")
        print("2. List")
        print("3. Find")
        print("4. Delete")
        print("5. Back")
        choice = input("Choose: ").strip()
        match choice:
            case '1': create_supplier_interactive()
            case '2': list_suppliers_interactive()
            case '3': find_supplier_interactive()
            case '4': delete_supplier_interactive()
            case '5': break
            case _: print("❌ Invalid choice.")

# ---------- MAIN MENU ----------

def main_menu():
    while True:
        print("\n📦 DELIVERY TRACKER CLI")
        print("1. Customers")
        print("2. Employees")
        print("3. Products")
        print("4. Orders")
        print("5. Order Details")
        print("6. Suppliers")
        print("7. Exit")
        choice = input("Choose an option: ").strip()

        match choice:
            case '1': customer_menu()
            case '2': employee_menu()
            case '3': product_menu()
            case '4': order_menu()
            case '5': order_detail_menu()
            case '6': supplier_menu()
            case '7':
                print("👋 Goodbye!")
                break
            case _: print("❌ Invalid option.")

# ---------- ENTRY POINT ----------

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n🛑 Interrupted. Exiting...")
