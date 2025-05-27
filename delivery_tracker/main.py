from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base

# Import all your model modules to ensure the tables are registered
from models import customer
from models import employee
from models import supplier
from models import product
from models import order
from models import order_detail

# Create the SQLite engine
engine = create_engine("sqlite:///delivery_tracker.db", echo=True)

# Create all tables in the database
Base.metadata.create_all(engine)

# Optional: Create a session factory
SessionLocal = sessionmaker(bind=engine)

if __name__ == "__main__":
    print("Database and tables created successfully.")
