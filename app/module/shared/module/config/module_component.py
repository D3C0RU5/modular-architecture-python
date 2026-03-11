class ModuleComponent:
    def __init__(self):
        self.sqlalchemy_modules: list = []

    def register_sqlalchemy(self, module):
        self.sqlalchemy_modules.append(module)

    def load_models(self):
        for module in self.sqlalchemy_modules:
            module.load_models()

    def migrations_paths(self):
        return [
            module.migrations_path
            for module in self.sqlalchemy_modules
            if module.migrations_path
        ]
