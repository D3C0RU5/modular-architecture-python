from fastapi import FastAPI

from app.module.template.module import TemplateModuleComponent

app = FastAPI(title="OneClick Modular App")

# Lista de módulos
modules = [
    TemplateModuleComponent(),
    # Outros módulos podem ser adicionados aqui
]

# Inicializa todos os módulos
for module in modules:
    module.init(app)
