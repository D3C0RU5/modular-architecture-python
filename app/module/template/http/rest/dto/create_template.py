from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class CreateTemplateRequestDTO(BaseModel):
    name: str = Field(min_length=3)


class TemplateResponseData(BaseModel):
    id: UUID
    name: str
    created_at: datetime | None


class TemplateResponse(BaseModel):
    state: str
    data: TemplateResponseData
