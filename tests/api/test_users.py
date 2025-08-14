import pytest

@pytest.mark.api
def test_get_user_1(api):
    r = api.get("/users/1")
    assert r.status_code == 200
    body = r.json()
    assert body["id"] == 1
    assert body["name"]  # no vacío

@pytest.mark.api
@pytest.mark.parametrize("uid", [1, 2, 3])
def test_users_parametrizados(api, uid):
    r = api.get(f"/users/{uid}")
    assert r.status_code == 200
    assert isinstance(r.json(), dict)
