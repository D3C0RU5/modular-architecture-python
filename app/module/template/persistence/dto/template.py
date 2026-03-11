from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from shared.module.persistence.sqlalchemy.base_dto import BaseDTO


class TemplateDTO(BaseDTO):
    id: UUID
    name: str
    created_at: datetime | None
    updated_at: datetime | None

    model_config = {"from_attributes": True}


@dataclass
class TemplateDTOData:
    id: UUID
    name: str
    created_at: datetime | None
    updated_at: datetime | None
