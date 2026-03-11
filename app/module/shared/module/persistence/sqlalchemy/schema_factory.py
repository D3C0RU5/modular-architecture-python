from sqlalchemy import text
from sqlalchemy.engine import Engine


class SchemaFactory:
    def __init__(self, name: str):
        self.name = name

    def table_args(self) -> dict:
        return {"schema": self.name}

    def create(self, engine: Engine):
        with engine.connect() as conn:
            conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {self.name}"))
            conn.commit()
