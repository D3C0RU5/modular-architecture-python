import importlib
import pkgutil

from shared.module.persistence.sqlalchemy.module_engine import ModuleEngine
from sqlalchemy.orm import sessionmaker


class SqlAlchemyModule:
    def __init__(
        self, models_package: str, database_url: str, engine: ModuleEngine | None = None
    ):
        self.models_package = models_package
        self.database_url = database_url
        self._engine = engine  # Pode receber engine existente
        self._SessionLocal = None

    def load_models(self):
        package = importlib.import_module(self.models_package)
        if hasattr(package, "__path__"):
            for _loader, modname, _ispkg in pkgutil.walk_packages(
                package.__path__, package.__name__ + "."
            ):
                importlib.import_module(modname)

    @property
    def engine(self) -> ModuleEngine:
        if self._engine is None:
            self._engine = ModuleEngine(self.database_url)
        return self._engine

    def get_session(self):
        if self._SessionLocal is None:
            self._SessionLocal = sessionmaker(
                bind=self.engine.engine, autoflush=False, autocommit=False
            )
        return self._SessionLocal()
