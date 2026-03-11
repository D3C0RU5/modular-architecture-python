from template.persistence.dao.template import TemplateDAO
from template.persistence.dto.template import TemplateDTOData


class ListAllTemplateUseCase:
    def __init__(self, dao: TemplateDAO):
        self.dao = dao

    def execute(self) -> list[TemplateDTOData]:
        list = self.dao.list_all()
        first = list[0]
        # first.
        return list
