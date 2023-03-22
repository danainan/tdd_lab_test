from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World_test"}

def test_read_name():
    response = client.get("/callname/Danainan")
    assert response.status_code == 200
    assert response.json() == {"hello": "Danainan"}

def test_post_name():
    response = client.post("/callname/Danainan")
    assert response.status_code == 200
    assert response.json() == {"hello": "Danainan"}
