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
        'username': 'testingemail@gmail.com',
        'password': 'TestPassword1_',
        'scope': 'openid profile email',
        'audience': 'https://welcome/',
        'client_id': 'PdkS09Ig0EYVGK9KPYwncjKMGzXnAasI'})
    return r.json()['access_token']


token = get_access_token()

auth_headers = {'Authorization': f'Bearer {token}'}
response = requests.get("https://secure-gorge-99048.herokuapp.com/api/application/last/", headers=auth_headers)
data = json.loads(response.text)
print(data)


def get_user_id():
    r = requests.get('https://suroegin503.eu.auth0.com/userinfo', headers=auth_headers)
    return r.json()['sub']


userId = get_user_id()


def test_not_authorized():
    response = client.get("/api/culture/prizes/")
    assert response.status_code == 401 or response.status_code == 403


def test_get_prize():
    response = client.get("/api/culture/prizes/", headers=auth_headers)
    assert response.status_code == 200
    assert type(response.json()) is list


def test_create_prize_check_user_id():
    response = client.post("/api/culture/prizes/", headers=auth_headers, data=json.dumps({
        "id": 0,
        "title": "string",
        "level": "string",
        "degree": "string",
        "place": 1,
        "date": "2021-05-13",
        "points": 1.0,
    }))

    assert response.status_code == 200
    body = response.json()
    assert type(body) is dict
    assert body['user_id'] == userId


def test_create_prize_with_incorrect_argument_returns_400():
    response = client.post("/api/culture/prizes/", headers=auth_headers, data=json.dumps({
        "id": 0,
        "title": "string",
        "level": "string",
        "degree": "string",
        "place": -1,
        "date": "2021-05-13",
        "points": 1.0,
    }))

    assert response.status_code // 100 == 4


def test_get_artwork():
    response = client.get("/api/culture/artworks/", headers=auth_headers)
    assert response.status_code == 200
    assert type(response.json()) is list


def test_create_artwork_check_user_id():
    response = client.post("/api/culture/artworks/", headers=auth_headers, data=json.dumps({
        "id": 0,
        "title": "string",
        "location": "string",
        "date": "2021-05-13",
        "points": 1.0,
    }))

    assert response.status_code == 200
    body = response.json()
    assert type(body) is dict
    assert body['user_id'] == userId


def test_get_activity():
    response = client.get("/api/culture/activity/", headers=auth_headers)
    assert response.status_code == 200
    assert type(response.json()) is list


def test_create_activity_check_user_id():
    response = client.post("/api/culture/activity/", headers=auth_headers, data=json.dumps({
        "id": 0,
        "title": "string",
        "work": "string",
        "level": "string",
        "date": "2021-05-13",
        "responsible": "string",
        "responsiblePosition": "string",
        "points": 1.0,
        "status": False,
    }))

    assert response.status_code == 200
    body = response.json()
    assert type(body) is dict
    assert body['user_id'] == userId
