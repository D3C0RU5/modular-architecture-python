from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker


class ModuleEngine:
    def __init__(self, database_url: str):
        self.database_url = database_url
        self._engine: Engine | None = None
        self._SessionLocal: sessionmaker | None = None

    @property
    def engine(self) -> Engine:
        if self._engine is None:
            self._engine = create_engine(self.database_url, future=True)
        return self._engine

    @property
    def SessionLocal(self) -> sessionmaker:
        if self._SessionLocal is None:
            self._SessionLocal = sessionmaker(
                autocommit=False, autoflush=False, bind=self.engine
            )
        return self._SessionLocal

    def get_session(self):
        """Factory de session"""
        return self.SessionLocal()
