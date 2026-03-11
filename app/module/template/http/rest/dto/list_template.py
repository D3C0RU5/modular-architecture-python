from typing import Any

from pydantic import BaseModel


class ListTemplatesResponse(BaseModel):
    state: str
    data: Any
