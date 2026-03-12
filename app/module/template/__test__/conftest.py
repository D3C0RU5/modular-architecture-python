import pytest
from fastapi.testclient import TestClient
from shared.module.persistence.sqlalchemy.base_model import Base
from sqlalchemy import text
from template.infra.db import engine
from template.module import template_module


@pytest.fixture(scope="module")
def app():
    from fastapi import FastAPI

    app = FastAPI()

    template_module.init(app)

    yield app


@pytest.fixture(scope="module")
def client(app):
    return TestClient(app)


@pytest.fixture(autouse=True)
def clean_db():
    def reset_db():
        Base.metadata.drop_all(bind=engine.get_engine)
        Base.metadata.create_all(bind=engine.get_engine)

        with engine.get_engine.connect() as conn:
            conn.execute(
                text(f"CREATE SCHEMA IF NOT EXISTS {template_module.SCHEMA_NAME}")
            )

    reset_db()
    yield
    reset_db()
