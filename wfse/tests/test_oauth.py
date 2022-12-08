from fastapi.testclient import TestClient

from wfse.app.main import create_app

testClient = TestClient(create_app())


def test_oauth_for_kakao_failed():
    response = testClient.get('/oauth/kakao')
    print('\n--------------')
    print(response)
    print('--------------')
    assert response.status_code == 404
    assert response.json() == {"!!!!": "!!!!"}


def test_oauth_for_kakao_successed():
    response = testClient.get('/oauth/kakao')
    print('\nstatus code in test ===>')
    print(response)
    assert response.status_code == 307
    # assert response.json() == {"code": ""}


def test_login_for_kakao_successed():
    code =  testClient.get('/oauth/kakao')
    response = testClient.get(f"/oauth/kakao/auth")
    print('\n--------------')
    print(response.json()['code'])
    print('--------------')
    assert response.status_code == 200
    assert response.json() == {"message": "welcome to Web For Simple Enjoy"}
