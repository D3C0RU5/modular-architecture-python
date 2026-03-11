# app/module/shared/module/config/module_component.py
from collections.abc import Callable

from fastapi import FastAPI
from sqlalchemy.engine import Engine


class ModuleComponent:
    def __init__(self, name: str, schema: str):
        self.name = name
        self.schema = schema
        self.router = None
        self.engine: Engine | None = None
        self.get_session: Callable | None = None

    def configure_engine(self, engine: Engine):
        self.engine = engine

    def configure_session(self, get_session: Callable):
        self.get_session = get_session

    def include_router(self, app: FastAPI):
        if self.router:
            app.include_router(self.router)
