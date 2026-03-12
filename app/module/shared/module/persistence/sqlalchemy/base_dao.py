from typing import Generic, TypeVar

from shared.module.persistence.sqlalchemy.has_from_model import ModelDTO
from shared.module.persistence.sqlalchemy.module_engine import ModuleEngine

T = TypeVar("T")
U = TypeVar("U", bound=ModelDTO)


class BaseDAO(Generic[T, U]):
    def __init__(self, model: type[T], dto_class: type[U], engine: ModuleEngine):
        self.model: type[T] = model
        self.dto_class: type[U] = dto_class
        self.engine = engine

    def list_all(self) -> list[U]:
        with self.engine.get_session() as session:
            return [
                self.dto_class.from_model(obj)
                for obj in session.query(self.model).all()
            ]

    def get_by_id(self, id) -> U | None:
        with self.engine.get_session() as session:
            obj = session.get(self.model, id)
            return self.dto_class.from_model(obj) if obj else None

    def create(self, object: U) -> U:
        with self.engine.get_session() as session:
            instance: T = object.to_model()
            session.add(instance)
            session.commit()
            session.refresh(instance)
            return self.dto_class.from_model(instance)

    def update(self, id, **kwargs) -> U | None:
        with self.engine.get_session() as session:
            obj: T | None = session.get(self.model, id)
            if not obj:
                return None
            for key, value in kwargs.items():
                setattr(obj, key, value)
            session.commit()
            session.refresh(obj)
            return self.dto_class.from_model(obj)

    def delete(self, id) -> None:
        with self.engine.get_session() as session:
            obj: T | None = session.get(self.model, id)
            if obj:
                session.delete(obj)
                session.commit()
