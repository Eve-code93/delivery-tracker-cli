import sys
import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# ─── Add the project root to sys.path ────────────────────────────────────────────
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# ─── Import Base and all models to enable Alembic's 'autogenerate' ───────────────
from models.base import Base
from models.customer import Customer
from models.employee import Employee
from models.supplier import Supplier
from models.product import Product
from models.order import Order
from models.order_detail import OrderDetail

# ─── Alembic Config object (from alembic.ini) ────────────────────────────────────
config = context.config

# ─── Configure Python logging from .ini file ─────────────────────────────────────
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ─── Set target metadata (needed for 'autogenerate') ─────────────────────────────
target_metadata = Base.metadata

# ─── Offline migrations (no DB connection required) ──────────────────────────────
def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

# ─── Online migrations (connects to DB) ──────────────────────────────────────────
def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

# ─── Entry point ─────────────────────────────────────────────────────────────────
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
