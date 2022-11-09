from fastapi.testclient import TestClient

from wfse.app.main import create_app

client = TestClient(create_app())


def test_read_main():
    response = client.get('')
    assert response.status_code == 200
    assert response.json() == {"message": "welcome to Web For Simple Enjoy"}
