import pytest
from fastapi.testclient import TestClient
from main import api

client = TestClient(api)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_create():
    payload = {
        "title": "sleep",
        "description": "I'll sleep at 11 pm"
    }
    response = client.post("/todo", json=payload)
    assert response.status_code == 200 
    assert response.json()["title"] == "sleep"
    assert response.json()["description"] == "I'll sleep at 11 pm"
