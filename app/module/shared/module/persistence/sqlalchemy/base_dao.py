from typing import Generic, TypeVar

from shared.module.persistence.sqlalchemy.has_from_model import HasFromModel
from shared.module.persistence.sqlalchemy.module_engine import ModuleEngine

T = TypeVar("T")
U = TypeVar("U", bound=HasFromModel)


class BaseDAO(Generic[T, U]):
    def __init__(self, model: type[T], dto_class: type[U], engine: ModuleEngine):
        self.model = model
        self.dto_class = dto_class
        self.engine = engine

    def list_all(self) -> list[U]:
        with self.engine.get_session() as session:
            return [
                self.dto_class.from_model(obj)
                for obj in session.query(self.model).all()
            ]
