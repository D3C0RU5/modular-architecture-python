from typing import (
    Protocol,
    Self,
)

from template.persistence.model.template import Template


class HasFromModel(Protocol):
    @classmethod
    def from_model(cls, model: Template) -> Self: ...
