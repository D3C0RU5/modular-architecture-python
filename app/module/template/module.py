from fastapi import FastAPI
from shared.module.persistence.sqlalchemy.sql_alchemy_module import SqlAlchemyModule
from sqlalchemy import text
from template.http.rest.controller.template_controller import router as template_router


class TemplateModuleComponent:
    def __init__(self):
        self.name = "template"
        self.schema = "templates"
        self.router = template_router
        self.sql_module = SqlAlchemyModule(
            models_package="template.persistence.model",
            database_url="postgresql+psycopg://admin:insecure@db:5432/oneclick",
        )

    def init(self, app: FastAPI):
        self.sql_module.load_models()

        with self.sql_module.engine.connect() as conn:
            conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {self.schema}"))

        app.include_router(self.router)
