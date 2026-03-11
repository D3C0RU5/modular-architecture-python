from typing import Annotated

from fastapi import APIRouter, status
from injectq.integrations.fastapi import InjectFastAPI
from template.http.rest.dto.create_template import (
    CreateTemplateRequestDTO,
    TemplateResponse,
)
from template.http.rest.dto.list_template import ListTemplatesResponse
from template.utils.di_container import (
    CreateTemplateUseCaseSingleton,
    ListAllTemplateUseCaseSingleton,
)

router = APIRouter(prefix="/templates", tags=["templates"])


@router.post("/", response_model=TemplateResponse, status_code=status.HTTP_201_CREATED)
def create_template(
    template: CreateTemplateRequestDTO,
    use_case: Annotated[
        CreateTemplateUseCaseSingleton, InjectFastAPI(CreateTemplateUseCaseSingleton)
    ],
):
    use_case.execute(name=template.name)
    return TemplateResponse(state="success", data=template.model_dump())


@router.get("/", response_model=ListTemplatesResponse)
def list_templates(
    use_case: Annotated[
        ListAllTemplateUseCaseSingleton, InjectFastAPI(ListAllTemplateUseCaseSingleton)
    ],
):
    templates = use_case.execute()
    data = [{"name": t.name, "created": t.created_at} for t in templates]
    return ListTemplatesResponse(state="success", data=data)
