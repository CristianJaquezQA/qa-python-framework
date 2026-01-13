import requests

class APIClient:
    """
    Simple HTTP client for practice purposes. We will use JSONPlaceholder,
    which is a public API for testing and experimentation.
    """

    def __init__(self, base_url: str = "https://jsonplaceholder.typicode.com", timeout: float = 5.0):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def get(self, path: str):
        url = f"{self.base_url}/{path.lstrip('/')}"
        return requests.get(url, timeout=self.timeout)
