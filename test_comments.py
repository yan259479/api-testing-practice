import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_status_3():
    response = requests.get(f"{BASE_URL}/comments/3")
    assert response.status_code == 200

def test_email():
    response = requests.get(f"{BASE_URL}/comments/3")
    data = response.json()
    assert 'email' in data

def test_status_none():
    response = requests.get(f"{BASE_URL}/comments/9999")
    assert response.status_code == 404