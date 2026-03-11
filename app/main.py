from fastapi import FastAPI

from app.module.template.module import TemplateModule

modules = [
    TemplateModule(),
]

app = FastAPI()

for module in modules:
    module.load_models()
