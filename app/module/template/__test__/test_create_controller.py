from fastapi import FastAPI
from fastapi.testclient import TestClient
from httpx import Response
from template.http.rest.controller.template_controller import router

app = FastAPI()
app.include_router(router)
client = TestClient(app)


def test_create_template():
    response: Response = client.post(
        "/templates", json={"name": "Teste", "content": "Conteúdo do template"}
    )
    assert response.status_code == 201
    assert response.json()["state"] == "success"
