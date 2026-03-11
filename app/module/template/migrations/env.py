from alembic import context
from shared.module.persistence.sqlalchemy import module_engine  # noqa: F401

from app.module.shared.module.persistence.sqlalchemy.base_model import BaseModel

config = context.config
target_metadata = BaseModel.metadata


def run_migrations_offline():
    """Executa migrations sem conexão com o banco."""
    url = config.get_main_option("sqlalchemy.url")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        include_schemas=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Executa migrations com conexão ativa."""
    engine = get_engine()

    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_schemas=True,
            version_table="alembic_version_template",
            version_table_schema="templates",
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
