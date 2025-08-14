import requests

class APIClient:
    """
    Cliente HTTP sencillo para practicar. Usaremos JSONPlaceholder,
    que es un API pública de prueba.
    """
    def __init__(self, base_url: str = "https://jsonplaceholder.typicode.com", timeout: float = 5.0):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def get(self, path: str):
        url = f"{self.base_url}/{path.lstrip('/')}"
        return requests.get(url, timeout=self.timeout)
