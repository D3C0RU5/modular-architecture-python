# shared/module/persistence/sqlalchemy/base_dao.py
from typing import Generic, TypeVar

from shared.module.persistence.sqlalchemy.module_engine import ModuleEngine

T = TypeVar("T")


class BaseDAO(Generic[T]):
    def __init__(self, model: type[T], engine: ModuleEngine):
        self.model = model
        self.engine = engine

    def create(self, **kwargs) -> T:
        with self.engine.get_session() as session:
            instance = self.model(**kwargs)
            session.add(instance)
            session.commit()
            session.refresh(instance)
            return instance

    def list_all(self) -> list[T]:
        with self.engine.get_session() as session:
            return session.query(self.model).all()

    def get_by_id(self, id) -> T | None:
        with self.engine.get_session() as session:
            return session.get(self.model, id)

    def delete(self, id) -> None:
        with self.engine.get_session() as session:
            obj = session.get(self.model, id)
            if obj:
                session.delete(obj)
                session.commit()
