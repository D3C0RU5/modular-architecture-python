from httpx import Response


def test_create_template(client):
    response: Response = client.post(
        "/templates", json={"name": "Teste", "content": "Conteúdo do template"}
    )
    assert response.status_code == 201
    assert response.json()["state"] == "success"


def test_create_template_with_empty_object(client):
    response: Response = client.post("/templates", json={})
    assert response.status_code == 422
