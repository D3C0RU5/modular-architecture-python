import os

from app.module.shared.module.persistence.sqlalchemy.module_engine import ModuleEngine

DATABASE_URL = os.getenv(
    "TEMPLATE_DATABASE_URL", "postgresql+psycopg://admin:insecure@db:5432/oneclick"
)

engine = ModuleEngine(DATABASE_URL)
get_engine = engine.engine
get_session = engine.get_session
