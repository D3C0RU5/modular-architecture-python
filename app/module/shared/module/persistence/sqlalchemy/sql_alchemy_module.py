from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class SqlAlchemyModule:
    def __init__(self, models_package: str, schema: str, migrations_path: str):
        self.models_package = models_package
        self.schema = schema
        self.migrations_path = migrations_path
        self._engine = None
        self._SessionLocal = None

    def load_models(self):
        import importlib

        importlib.import_module(self.models_package)

    @property
    def engine(self):
        """Retorna a engine SQLAlchemy"""
        if self._engine is None:
            # engine_url precisa ser passado aqui ou configurado externamente
            from app.module.template.infra.db.engine import DATABASE_URL

            self._engine = create_engine(DATABASE_URL, future=True)
        return self._engine

    @property
    def session(self):
        """Factory de session"""
        if self._SessionLocal is None:
            self._SessionLocal = sessionmaker(
                bind=self.engine, autoflush=False, autocommit=False
            )
        return self._SessionLocal

    def get_session(self):
        return self.session()
