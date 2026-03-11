import importlib
import pkgutil

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class SqlAlchemyModule:
    def __init__(self, models_package: str, database_url: str):
        self.models_package = models_package
        self.database_url = database_url
        self._engine = None
        self._SessionLocal = None

    def load_models(self):

        package = importlib.import_module(self.models_package)

        if hasattr(package, "__path__"):
            for _loader, modname, _ispkg in pkgutil.walk_packages(
                package.__path__, package.__name__ + "."
            ):
                importlib.import_module(modname)

    @property
    def engine(self):
        if self._engine is None:
            self._engine = create_engine(self.database_url, future=True)
        return self._engine

    def get_session(self):
        if self._SessionLocal is None:
            self._SessionLocal = sessionmaker(
                bind=self.engine, autoflush=False, autocommit=False
            )
        return self._SessionLocal()
