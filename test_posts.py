import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200

def test_user_has_name():
    response = requests.get(f"{BASE_URL}/posts/1")
    data = response.json()
    assert "title" in data