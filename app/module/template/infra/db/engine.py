import os

from app.module.shared.module.persistence.sqlalchemy.module_engine import ModuleEngine

DATABASE_URL = os.getenv(
    "TEMPLATE_DATABASE_URL", "postgresql+psycopg://admin:insecure@db:5432/oneclick"
)

# Engine do módulo
module_engine = ModuleEngine(DATABASE_URL)
get_engine = module_engine.engine
get_session = module_engine.get_session
