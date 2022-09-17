from fastapi.testclient import TestClient
from fastapi import FastAPI

client = TestClient(FastAPI())



def test_find_all_recipes():
    response = client.get("/")
    assert response.status_code == 404
