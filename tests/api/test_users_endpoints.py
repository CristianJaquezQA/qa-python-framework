# tests/api/test_users_endpoints.py
import requests
import pytest
import json
BASE = "https://jsonplaceholder.typicode.com"  # cámbialo por tu API
TIMEOUT = 10

def test_users_get_by_id_ok():
    r = requests.get(f"{BASE}/users/1", timeout=TIMEOUT)
    print(r.text)
    assert r.status_code == 200
    assert r.headers.get("Content-Type", "").startswith("application/json")
    data = r.json()
    print(json.dumps(data, indent=4, sort_keys=True))
    assert data["id"] == 1
    assert "name" in data and "email" in data

def test_users_list_filters_by_username():
    r = requests.get(f"{BASE}/users", params={"username": "Bret"}, timeout=TIMEOUT)
    assert r.status_code == 200
    data = r.json()
    print(json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False))
    assert isinstance(data, list)
    assert any(u.get("username") == "Bret" for u in data)

def test_create_post_returns_201_and_body():
    payload = {"title": "demo", "body": "contenido", "userId": 1}
    r = requests.post(f"{BASE}/posts", json=payload, timeout=TIMEOUT)
    assert r.status_code in (200, 201)
    body = r.json()
    assert body["title"] == payload["title"]
    assert "id" in body  # el backend asigna un id

def test_update_post_put_idempotent():
    payload = {"id": 1, "title": "nuevo", "body": "texto", "userId": 1}
    r = requests.put(f"{BASE}/posts/1", json=payload, timeout=TIMEOUT)
    assert r.status_code in (200, 204)
    if r.status_code == 200:
        assert r.json()["title"] == "nuevo"

def test_delete_post_returns_200_or_204():
    r = requests.delete(f"{BASE}/posts/1", timeout=TIMEOUT)
    assert r.status_code in (200, 204)
