from sqlalchemy.orm import sessionmaker

from .module_engine import engine

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)
