
from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.json["project"] == (
        "DevOps Automation and Deployment Pipeline"
    )
    assert response.json["status"] == "success"


def test_health():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json == {
        "status": "healthy",
        "version": "1.2"
    }


def test_not_found():
    client = app.test_client()
    response = client.get("/invalid-route")

    assert response.status_code == 404
