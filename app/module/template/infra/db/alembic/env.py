from template.module import TemplateModuleComponent

from app.module.shared.module.persistence.sqlalchemy.alembic_runner import (
    AlembicModuleRunner,
)

template_module = TemplateModuleComponent()

runner = AlembicModuleRunner(template_module)

runner.run()
