import sqlite3

db_path = 'delivery_tracker.db'  # or your actual DB path

conn = sqlite3.connect(db_path)
conn.execute('DROP TABLE IF EXISTS _alembic_tmp_customers;')
conn.commit()
conn.close()

print("Temporary table _alembic_tmp_customers dropped successfully.")
