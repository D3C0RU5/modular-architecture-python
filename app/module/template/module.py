# app/module/template/module_component.py
from fastapi import FastAPI
from shared.module.config.module_component import ModuleComponent
from shared.module.persistence.sqlalchemy.sql_alchemy_module import SqlAlchemyModule
from sqlalchemy import text

from app.module.template.http.rest.controller.template_controller import (
    router as template_router,
)


class TemplateModuleComponent(ModuleComponent):
    def __init__(self):
        super().__init__(name="template", schema="templates")
        self.router = template_router
        # instancia do SqlAlchemyModule específico do módulo
        self.sql_module = SqlAlchemyModule(
            models_package="app.module.template.persistence.model",
            schema=self.schema,
            migrations_path="app/module/template/migrations",
        )

    def init(self, app: FastAPI):
        # Carrega os models do módulo
        self.sql_module.load_models()

        # Configura engine e session
        self.configure_engine(lambda: self.sql_module.engine)
        self.configure_session(self.sql_module.get_session)  # ⚡ método get_session

        # Cria schema se não existir
        assert self.engine is not None
        with self.engine.connect() as conn:  # ⚡ engine já inicializada
            conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {self.schema}"))

        # Registra router no FastAPI
        self.include_router(app)
