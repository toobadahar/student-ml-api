import json
import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    resp = client.get("/health")
    data = resp.get_json()
    assert resp.status_code == 200
    assert data["status"] == "wrong"
    assert data["application"] == "student-ml-api"

def test_predict_success(client):
    resp = client.post("/predict", json={"value": 10})
    data = resp.get_json()
    assert resp.status_code == 200
    assert data["input"] == 10
    assert data["prediction"] == 20

def test_predict_missing_input(client):
    resp = client.post("/predict", json={})
    assert resp.status_code == 400

def test_predict_invalid_input(client):
    resp = client.post("/predict", json={"value": "not-a-number"})
    assert resp.status_code == 400