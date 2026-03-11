from fastapi import FastAPI
from template.module import TemplateModuleComponent

app = FastAPI()

template_module = TemplateModuleComponent().init(app)
