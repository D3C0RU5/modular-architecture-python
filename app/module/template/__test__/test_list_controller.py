from fastapi import FastAPI
from fastapi.testclient import TestClient
from template.http.rest.controller.template_controller import router

app = FastAPI()
app.include_router(router)
client = TestClient(app)


def test_list_templates(client):
    response = client.get("/templates")
    assert response.status_code == 200
    assert response.json()["state"] == "success"
