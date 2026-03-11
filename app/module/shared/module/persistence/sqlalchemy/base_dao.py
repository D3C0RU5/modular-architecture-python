# shared/module/persistence/sqlalchemy/base_dao.py
from typing import Generic, TypeVar

from shared.module.persistence.sqlalchemy.base_dto import BaseDTO
from shared.module.persistence.sqlalchemy.module_engine import ModuleEngine

T = TypeVar("T")  # SQLAlchemy model
U = TypeVar("U", bound=BaseDTO)  # DTO Pydantic
V = TypeVar("V")  # TypedDict de retorno


class BaseDAO(Generic[T, U, V]):
    def __init__(
        self, model: type[T], dto: type[U], typed: type[V], engine: ModuleEngine
    ):
        self.model = model
        self.dto = dto
        self.typed = typed
        self.engine = engine

    def create(self, **kwargs) -> U:
        with self.engine.get_session() as session:
            instance = self.model(**kwargs)
            session.add(instance)
            session.commit()
            session.refresh(instance)
            return self.dto.model_validate(instance)

    def list_all(self) -> list[V]:
        with self.engine.get_session() as session:
            return [
                self.typed(**self.dto.model_validate(obj).model_dump())
                for obj in session.query(self.model).all()
            ]

    def get_by_id(self, id) -> U | None:
        with self.engine.get_session() as session:
            obj = session.get(self.model, id)
            return self.dto.model_validate(obj) if obj else None

    def delete(self, id) -> None:
        with self.engine.get_session() as session:
            obj = session.get(self.model, id)
            if obj:
                session.delete(obj)
                session.commit()
