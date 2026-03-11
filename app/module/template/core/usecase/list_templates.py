from template.persistence.dao.template import TemplateDAO
from template.persistence.model.template import Template


class ListAllTemplateUseCase:
    def __init__(self, dao: TemplateDAO):
        self.dao = dao

    def execute(self) -> list[Template]:
        return self.dao.list_all()
