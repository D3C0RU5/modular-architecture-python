from shared.module.persistence.sqlalchemy.alembic_runner import AlembicModuleRunner
from template.module import TemplateModuleComponent

template_module = TemplateModuleComponent()

runner = AlembicModuleRunner(template_module)

runner.run()
