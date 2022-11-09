from fastapi.testclient import TestClient

from wfse.app.main import create_app


class TestCase:
    ip: str = '192.168.0.12'


client = TestClient(create_app())


def test_fortune_pass():
    response = client.get('/fortune/')
    assert response.status_code == 200
    assert response.json() == {'message': 'here is fortune'}


def test_fortune_fail():
    response = client.get('/fortune/')
    assert response.status_code == 400
    assert response.json() == {'message': 'fortune'}


def test_fortune_checking():
    response = client.get('/fortune/checking')
    response_body = response.json()
    print(f'{response_body}')
    assert response.status_code == 200
    assert response.json() == {'message': 'here is fortune checking'}


def test_fortune_result():
    response = client.get(f'/fortune/result/{TestCase.ip}')
    response_body = response.json()
    print(f'\n{response_body}')
    assert response.status_code == 201
    assert 'Feeling' in response_body.keys()


def test_fortune_invalid_result():
    response = client.get('/fortune/result')
    response_body = response.json()
    assert response.status_code == 400
    assert 'INVALID_REQUEST' == response_body["msg"]