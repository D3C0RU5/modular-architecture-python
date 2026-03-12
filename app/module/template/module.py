from fastapi import FastAPI
from injectq.integrations.fastapi import setup_fastapi
from shared.module.persistence.sqlalchemy.sql_alchemy_module import SqlAlchemyModule
from sqlalchemy import text
from template.http.rest.controller.template_controller import router as template_router
from template.infra.db.engine import module_engine
from template.utils.di_container import container


class TemplateModuleComponent:
    SCHEMA_NAME = "templates"

    def __init__(self):
        self.name = "template"
        self.router = template_router

        self.sql_module = SqlAlchemyModule(
            models_package="template.persistence.model",
            database_url=module_engine.database_url,
            engine=module_engine,
        )

    def init(self, app: FastAPI):
        self.sql_module.load_models()

        with module_engine.engine.connect() as conn:
            conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {self.SCHEMA_NAME}"))

        setup_fastapi(container, app)
        app.include_router(self.router)


template_module = TemplateModuleComponent()
