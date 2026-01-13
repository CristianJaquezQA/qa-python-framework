# tests/api/test_crud_examples.py
import requests

BASE = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10


def test_get_user_by_id():
    r = requests.get(f"{BASE}/users/1", timeout=TIMEOUT)
    assert r.status_code == 200
    assert r.headers["Content-Type"].startswith("application/json")
    data = r.json()
    assert data["id"] == 1
    assert "name" in data and "email" in data


def test_post_create_post():
    payload = {"title": "hello", "body": "test post", "userId": 1}
    r = requests.post(f"{BASE}/posts", json=payload, timeout=TIMEOUT)
    assert r.status_code in (200, 201)  # JSONPlaceholder usually returns 201
    assert r.headers["Content-Type"].startswith("application/json")
    data = r.json()
    # The API returns the echoed payload plus a generated id (e.g. 101)
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data


def test_put_update_post():
    payload = {"id": 1, "title": "updated", "body": "content", "userId": 1}
    r = requests.put(f"{BASE}/posts/1", json=payload, timeout=TIMEOUT)
    assert r.status_code in (200, 204)
    # JSONPlaceholder returns 200 with the updated resource as JSON
    if r.status_code == 200:
        assert r.headers["Content-Type"].startswith("application/json")
        data = r.json()
        assert data["id"] == 1
        assert data["title"] == "updated"


def test_delete_post():
    r = requests.delete(f"{BASE}/posts/1", timeout=TIMEOUT)
    assert r.status_code in (200, 204)
    # JSONPlaceholder usually returns 200 with an empty JSON object
    if r.status_code == 200:
        assert r.headers["Content-Type"].startswith("application/json")
        assert r.json() == {}


