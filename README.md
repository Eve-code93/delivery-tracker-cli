
Delivery Tracker CLI is a lightweight, terminal-based app designed to simplify delivery logistics. It lets you record and manage customers, products, orders, and delivery statuses—without the clutter.

✨ Features
Customer Management – Add, view, and update customer records.

Order Tracking – Create and monitor orders with delivery statuses.

Status Updates – Quickly mark orders as Pending, In Transit, Delivered, etc.

Product Catalog – Manage products and their suppliers.

CLI Powered by Click – Easy-to-use, extensible command-line interface.

SQLite + SQLAlchemy – Fast local database for persistent storage.

Database Migrations with Alembic – Easily evolve the schema as your app grows.

🗂️ Project Structure
bash
Copy
Edit
delivery_tracker/
├── alembic/            # Alembic migration files
├── cli/                # CLI command modules
│   ├── __init__.py
│   ├── customer.py
│   ├── order.py
│   └── product.py
├── db/                 # Database configuration
│   └── session.py
├── models/             # SQLAlchemy models
│   ├── base.py
│   ├── customer.py
│   ├── employee.py
│   ├── order.py
│   ├── order_detail.py
│   ├── product.py
│   └── supplier.py
├── insert_data.py      # Example script to add sample data
├── main.py             # CLI entry point
├── config.py           # Database settings
├── alembic.ini         # Alembic config
├── delivery_tracker.db # SQLite database (auto-created)
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies
🛠️ Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/Eve-code93/delivery-tracker-cli.git
cd delivery-tracker-cli/delivery_tracker
2. Create and Activate Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Linux/macOS
# OR
venv\Scripts\activate  # Windows
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run Database Migrations
bash
Copy
Edit
alembic upgrade head
This will generate the SQLite database and required tables.

⚙️ Using the CLI
All commands are accessed through the main.py CLI entry point:

bash
Copy
Edit
python main.py
🔹 Available Commands
bash
Copy
Edit
python main.py --help

Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  customer   Manage customers
  order      Manage orders
  product    Manage products
➕ Add a New Customer
bash
Copy
Edit
python main.py customer add --name "Alice Smith" --email "alice@example.com" --address "123 Nairobi Rd"
➕ Add a New Order
bash
Copy
Edit
python main.py order add --customer-id 1 --product-id 2 --quantity 3 --status "Pending"
🔍 View Orders
bash
Copy
Edit
python main.py order list
📊 Sample Data
To insert example records into the database, run:

bash
Copy
Edit
python insert_data.py
🔄 Database Migrations (Alembic)
To generate a new migration after updating models:

bash
Copy
Edit
alembic revision --autogenerate -m "Describe your change"
alembic upgrade head
🧪 Testing (Optional)
You can add test scripts under a tests/ directory using pytest or basic test files.

🙋‍♀️ Contributing
Contributions are welcome! You can:

Add new CLI features

Improve database relationships

Write unit tests

Suggest UI/UX improvements for CLI usage

📌 Notes
Currently using SQLite for simplicity, but can be easily switched to PostgreSQL or MySQL by editing config.py and alembic.ini.

Modular CLI design allows for future GUI or web integrations.
