import pytest
from src.api.client import APIClient
from src.ui.driver import build_driver


@pytest.fixture(scope="session")
def api():
    # Practice API client (JSONPlaceholder)
    return APIClient()


@pytest.fixture
def driver():
    # Create and close the browser for each UI test
    d = build_driver()
    try:
        yield d
    finally:
        d.quit()

