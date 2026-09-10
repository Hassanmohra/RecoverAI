from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["name"] == "RecoverAI"

def test_health():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_devices():
    response = client.get("/api/devices")
    assert response.status_code == 200
    assert response.json()["status"] == "success"
