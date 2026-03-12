from typing import Protocol, Self, TypeVar

TModel = TypeVar("TModel")


class ModelDTO(Protocol[TModel]):
    @classmethod
    def from_model(cls, model: TModel) -> Self: ...

    def to_model(self) -> TModel: ...
