from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Replace this with your actual DB URL
DATABASE_URL = "sqlite:///./delivery_tracker.db"  # Example: SQLite file-based DB

engine = create_engine(DATABASE_URL, echo=True)  # echo=True to log SQL queries

# SessionLocal class will be used to create session instances
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
