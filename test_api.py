import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_user():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200

def test_user_has_name():
    response = requests.get(f"{BASE_URL}/users/1")
    data = response.json()
    assert "name" in data

def test_get_invalid_user():
    response = requests.get(f"{BASE_URL}/users/9999")
    assert response.status_code == 404
