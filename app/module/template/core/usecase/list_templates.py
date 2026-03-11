from template.persistence.dao.template import TemplateDAO
from template.persistence.dto.template import TemplateDTO


class ListAllTemplateUseCase:
    def __init__(self, dao: TemplateDAO):
        self.dao = dao

    def execute(self) -> list[TemplateDTO]:
        list = self.dao.list_all()
        return list
