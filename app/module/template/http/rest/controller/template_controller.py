from fastapi import APIRouter, status
from template.http.rest.dto.create_template import (
    CreateTemplateRequestDTO,
    TemplateResponse,
)

router = APIRouter(prefix="/templates", tags=["templates"])


@router.post("/", response_model=TemplateResponse, status_code=status.HTTP_201_CREATED)
def create_template(template: CreateTemplateRequestDTO):
    return TemplateResponse(state="success", data=template.model_dump())


@router.get("/", response_model=TemplateResponse)
def list_templates():
    templates = {"name": "Template 1", "content": "Conteúdo 1"}

    return TemplateResponse(state="success", data=templates)
