from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "DevOps Homework App is Running!", "version": "1.0.0"}

def test_create_task():
    response = client.post("/tasks", json={"title": "Test Task", "description": "DevOps"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"