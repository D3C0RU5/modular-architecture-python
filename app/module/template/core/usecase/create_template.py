import uuid

from template.persistence.dao.template import TemplateDAO
from template.persistence.model.template import Template


class CreateTemplateUseCase:
    def __init__(self, dao: TemplateDAO):
        self.dao = dao

    def execute(self, name: str) -> Template:
        entity = Template(id=uuid.uuid4(), name=name)

        self.dao.create(id=entity.id, name=entity.name)

        return entity
