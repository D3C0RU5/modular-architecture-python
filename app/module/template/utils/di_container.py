from injectq import InjectQ, singleton
from template.core.usecase.create_template import CreateTemplateUseCase
from template.core.usecase.list_templates import ListAllTemplateUseCase
from template.persistence.dao.template import TemplateDAO

container = InjectQ.get_instance()


@singleton
class TemplateDAOSingleton(TemplateDAO):
    pass


@singleton
class CreateTemplateUseCaseSingleton(CreateTemplateUseCase):
    def __init__(self, dao: TemplateDAOSingleton):
        super().__init__(dao)


@singleton
class ListAllTemplateUseCaseSingleton(ListAllTemplateUseCase):
    def __init__(self, dao: TemplateDAOSingleton):
        super().__init__(dao)
