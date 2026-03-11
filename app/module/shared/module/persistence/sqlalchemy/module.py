import importlib


class SqlAlchemyModule:
    def __init__(
        self,
        models_package: str,
        schema: str | None = None,
        migrations_path: str | None = None,
    ):
        self.models_package = models_package
        self.schema = schema
        self.migrations_path = migrations_path

    def load_models(self):
        importlib.import_module(self.models_package)

    def table_args(self):
        if self.schema:
            return {"schema": self.schema}

        return {}
