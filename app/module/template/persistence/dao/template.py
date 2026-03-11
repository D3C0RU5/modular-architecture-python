from shared.module.persistence.sqlalchemy.base_dao import BaseDAO
from template.infra.db.engine import module_engine
from template.persistence.dto.template import TemplateDTO, TemplateDTOData
from template.persistence.model.template import Template


class TemplateDAO(BaseDAO[Template, TemplateDTO, TemplateDTOData]):
    def __init__(self):
        super().__init__(Template, TemplateDTO, TemplateDTOData, module_engine)
