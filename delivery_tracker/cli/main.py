import sys
from cli.customer_cli import customer_cli
from cli.employee_cli import employee_cli
from cli.order_cli import order_cli
from cli.order_detail_cli import order_detail_cli
from cli.product_cli import product_cli
from cli.supplier_cli import supplier_cli

def show_main_menu():
    print("\n--- Delivery Tracker CLI ---")
    print("Select an entity to manage:")
    print("1. Customers")
    print("2. Employees")
    print("3. Orders")
    print("4. Order Details")
    print("5. Products")
    print("6. Suppliers")
    print("0. Exit")

def show_entity_menu(entity_name):
    print(f"\n--- Manage {entity_name} ---")
    print("1. Create")
    print("2. Delete")
    print("3. List All")
    print("4. Find by attribute")
    print("5. View related objects")
    print("0. Back to main menu")

def input_choice(prompt, valid_choices):
    choice = input(prompt).strip()
    while choice not in valid_choices:
        print("Invalid choice. Please try again.")
        choice = input(prompt).strip()
    return choice

def run_interactive():
    while True:
        show_main_menu()
        choice = input_choice("Enter choice: ", ['0','1','2','3','4','5','6'])
        if choice == '0':
            print("Goodbye!")
            sys.exit(0)

        entity_map = {
            '1': ('Customers', customer_cli),
            '2': ('Employees', employee_cli),
            '3': ('Orders', order_cli),
            '4': ('Order Details', order_detail_cli),
            '5': ('Products', product_cli),
            '6': ('Suppliers', supplier_cli),
        }

        entity_name, cli_group = entity_map[choice]

        while True:
            show_entity_menu(entity_name)
            action = input_choice("Choose action: ", ['0','1','2','3','4','5'])
            if action == '0':
                break  # Back to main menu

            # Here, instead of invoking Click commands directly (which is tricky),
            # you should call the underlying business logic functions for that entity.
            # For now, just a placeholder print:
            print(f"You chose to {['Create','Delete','List All','Find','View Related'][int(action)-1]} {entity_name}")

            # TODO: Call the appropriate function for each action, e.g.:
            # if entity_name == 'Customers' and action == '1':
            #     create_customer_interactive()
            # Implement input prompts and validations inside those functions.

def main():
    import click

    @click.group()
    def cli():
        """Delivery Tracker CLI - Manage customers, employees, orders, and more."""
        pass

    # Register existing CLI subcommands for normal CLI usage
    cli.add_command(customer_cli, name='customer-cli')
    cli.add_command(employee_cli, name='employee-cli')
    cli.add_command(order_cli, name='order-cli')
    cli.add_command(order_detail_cli, name='order-detail-cli')
    cli.add_command(product_cli, name='product-cli')
    cli.add_command(supplier_cli, name='supplier-cli')

    @cli.command()
    def interactive():
        """Run the interactive menu-driven CLI."""
        run_interactive()

    cli()

if __name__ == "__main__":
    main()
