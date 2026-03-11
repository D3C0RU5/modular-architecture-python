from alembic import context
from shared.module.persistence.sqlalchemy.base_model import Base
from sqlalchemy import text
from sqlalchemy.engine import Engine


class AlembicModuleRunner:
    def __init__(self, module_component):
        self.module = module_component
        self.metadata = Base.metadata
        self.config = context.config

        self.module.sql_module.load_models()

    def run_offline(self):
        url = self.config.get_main_option("sqlalchemy.url")
        context.configure(
            url=url,
            target_metadata=self.metadata,
            literal_binds=True,
            include_schemas=True,
            compare_type=True,
        )
        with context.begin_transaction():
            context.run_migrations()

    def run_online(self):
        engine: Engine = self.module.sql_module.engine
        with engine.connect() as connection:
            connection.execute(
                text(f"CREATE SCHEMA IF NOT EXISTS {self.module.schema}")
            )
            connection.commit()

            context.configure(
                connection=connection,
                target_metadata=self.metadata,
                include_schemas=True,
                version_table=f"alembic_version_{self.module.name}",
                version_table_schema=self.module.schema,
                compare_type=True,
            )

            with context.begin_transaction():
                context.run_migrations()

    def run(self):
        if context.is_offline_mode():
            self.run_offline()
        else:
            self.run_online()
