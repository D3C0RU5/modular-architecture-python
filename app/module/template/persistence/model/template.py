from shared.module.persistence.sqlalchemy.base_model import BaseModel
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class Template(BaseModel):
    __tablename__ = "templates"
    __table_args__ = {"schema": "templates"}

    name: Mapped[str] = mapped_column(String(255))
