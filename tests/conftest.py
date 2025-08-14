import pytest
from src.api.client import APIClient
from src.ui.driver import build_driver

@pytest.fixture(scope="session")
def api():
    # Cliente API de práctica (JSONPlaceholder)
    return APIClient()

@pytest.fixture
def driver():
    # Crea y cierra el navegador por cada test de UI
    d = build_driver()
    try:
        yield d
    finally:
        d.quit()
