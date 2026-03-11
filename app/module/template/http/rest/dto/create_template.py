from typing import Any

from pydantic import BaseModel, Field


class CreateTemplateRequestDTO(BaseModel):
    name: str = Field(min_length=3)


class TemplateResponse(BaseModel):
    state: str
    data: dict[str, Any]
