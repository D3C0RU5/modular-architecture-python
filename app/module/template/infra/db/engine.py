import os

from dotenv import load_dotenv

from app.module.shared.module.persistence.sqlalchemy.module_engine import ModuleEngine

load_dotenv()

DATABASE_URL = os.getenv(
    "TEMPLATE_DATABASE_URL", "postgresql+psycopg://admin:insecure@db:5432/oneclick"
)

module_engine = ModuleEngine(DATABASE_URL)
get_engine = module_engine.engine
get_session = module_engine.get_session
