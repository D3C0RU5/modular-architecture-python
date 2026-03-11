from shared.module.config.module_component import ModuleComponent
from shared.module.persistence.sqlalchemy.module import SqlAlchemyModule


class TemplateModule(ModuleComponent):
    def __init__(self):
        super().__init__()

        self.register_sqlalchemy(
            SqlAlchemyModule(
                models_package="app.module.template.persistence.model.template",
                schema="templates",
                migrations_path="app/module/template/migrations",
            )
        )
