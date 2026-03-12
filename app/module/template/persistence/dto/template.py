# template/persistence/dto/template.py
from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Self
from uuid import UUID

from template.persistence.model.template import Template


@dataclass
class TemplateDTO:
    id: UUID
    name: str
    created_at: datetime | None
    updated_at: datetime | None

    @classmethod
    def from_model(cls, model: Template) -> Self:
        return cls(
            id=model.id,
            name=model.name,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )

    def to_model(self) -> Template:
        return Template(
            id=self.id,
            name=self.name,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    def to_dict(self) -> dict:
        return asdict(self)
