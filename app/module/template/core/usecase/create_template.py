import uuid

from template.persistence.dao.template import TemplateDAO
from template.persistence.dto.template import TemplateDTO


class CreateTemplateUseCase:
    def __init__(self, dao: TemplateDAO):
        self.dao = dao

    def execute(self, name: str) -> TemplateDTO:
        input_dto = TemplateDTO(
            id=uuid.uuid4(),
            name=name,
            created_at=None,
            updated_at=None,
        )

        created = self.dao.create(object=input_dto)

        return created
