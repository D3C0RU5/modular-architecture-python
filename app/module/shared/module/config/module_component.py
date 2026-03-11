# shared/module/config/module_component.py
from collections.abc import Callable

from fastapi import APIRouter
from sqlalchemy.orm import sessionmaker


class ModuleComponent:
    """Base para implementação de módulo"""

    def __init__(self, name: str, schema: str):
        self.name = name
        self.schema = schema
        self.router: APIRouter | None = None
        self.engine = None
        self.SessionLocal: sessionmaker | None = None

    def configure_engine(self, engine_factory: Callable):
        self.engine = engine_factory()

    def configure_session(self, session_factory: Callable):
        self.SessionLocal = session_factory()

    def get_session(self):
        if not self.SessionLocal:
            raise RuntimeError(f"Session não configurada para {self.name}")
        return self.SessionLocal()

    def include_router(self, app):
        if self.router:
            app.include_router(self.router, prefix=f"/{self.name}")

    def init(self, app):
        """Método que cada módulo deve implementar para inicialização"""
        raise NotImplementedError()
