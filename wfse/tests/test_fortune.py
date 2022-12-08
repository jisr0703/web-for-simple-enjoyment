from fastapi.testclient import TestClient

from wfse.app.main import create_app


class TestCase:
    new_ip: str = '192.168.0.101'
    exist_ip: str = '192.168.0.111'


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
    assert response.json() == {'hi': 'here is fortune checking'}


def test_fortune_checking_testing():
    print()
    response = client.get(f'/fortune/checking/test?feeling_id={1}')
    print(response)
    response_body = response.json()
    print(f'{response_body}')
    assert response.status_code == 200
    assert response.json() == {'message': 'here is fortune checking'}


def test_fortune_result():
    response = client.get(f'/fortune/result/{TestCase.new_ip}')
    response_body = response.json()
    assert response.status_code == 201
    assert 'Feeling' in response_body.keys() and response_body['exist'] == False


def test_fortune_exist_result():
    response = client.get(f'/fortune/result/{TestCase.exist_ip}')
    response_body = response.json()
    assert response.status_code == 201
    assert 'feeling' in response_body.keys() and response_body['exist'] == True


def test_fortune_invalid_result():
    response = client.get('/fortune/result')
    response_body = response.json()
    assert response.status_code == 404
    assert 'INVALID_REQUEST' == response_body["msg"]
