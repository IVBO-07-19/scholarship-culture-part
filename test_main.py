import requests
from fastapi.testclient import TestClient
from app.main import app
import json

client = TestClient(app)


# url = "/api/culture/prizes/"
# to database.py: config = configparser.ConfigParser()
# config.read("config.ini"), SQLALCHEMY_DATABASE_URL = config["test"]["url"]


def get_access_token():
    r = requests.post('https://suroegin503.eu.auth0.com/oauth/token', data={
        'grant_type': 'password',
        'username': 'test1@mail.ru',
        'password': '123321',
        'scope': 'openid profile email',
        'audience': 'https://welcome/',
        'client_id': 'PdkS09Ig0EYVGK9KPYwncjKMGzXnAasI'})
    return r.json()['access_token']


token = get_access_token()

auth_headers = {'Authorization': f'Bearer {token}'}


def get_user_id():
    r = requests.get('https://suroegin503.eu.auth0.com/userinfo', headers=auth_headers)
    return r.json()['sub']


userId = get_user_id()


def test_not_authorized():
    response = client.get("/api/culture/prizes/")
    assert response.status_code == 401 or response.status_code == 403


def test_get_article_writers():
    response = client.get("/api/culture/prizes/", headers=auth_headers)
    assert response.status_code == 200
    assert type(response.json()) is list


def test_create_article_writer_check_user_id():
    response = client.post("/api/culture/prizes/", headers=auth_headers, data=json.dumps({
        "id": 0,
        "title": "string",
        "level": 0,
        "degree": 0,
        "place": 0,
        "date": "2021-05-13",
        "points": 0,
        "id_request": "string"
    }))

    assert response.status_code == 200
    body = response.json()
    assert type(body) is dict
    assert body['user_id'] == userId


def test_create_article_writer_with_incorrect_argument_returns_400():
    response = client.post("/api/culture/prizes/", headers=auth_headers, data=json.dumps({
        "id": 0,
        "title": "string",
        "level": 0,
        "degree": 0,
        "place": -1,
        "date": "2021-05-13",
        "points": 0,
        "id_request": "string"
    }))

    assert response.status_code % 100 == 4
