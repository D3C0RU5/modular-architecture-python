from alembic import context
from sqlalchemy import text
from template.module import TemplateModuleComponent

from app.module.shared.module.persistence.sqlalchemy.base_model import BaseModel

config = context.config
target_metadata = BaseModel.metadata

# Cria a instância do módulo
template_module = TemplateModuleComponent()


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
    # Cria engine e conecta
    engine = template_module.sql_module.engine
    with engine.connect() as connection:
        # Cria schema se não existir
        connection.execute(
            text(f"CREATE SCHEMA IF NOT EXISTS {template_module.schema}")
        )
        # connection.commit()  # opcional, SQLAlchemy 2.x já usa transação context

        # Configura Alembic
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_schemas=True,
            version_table="alembic_version_template",
            version_table_schema=template_module.schema,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
