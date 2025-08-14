import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest

def build_driver():
    """
    Driver mínimo:
    - Headless activable con HEADLESS=true (útil para CI).
    - Tamaño de ventana fijo para evitar diferencias de layout.
    """
    opts = Options()
    is_headless = os.getenv("HEADLESS","").strip().lower()
    if is_headless in ("1", "true", "yes"):
        print("Headless activated")
        opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1280,1600")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-gpu")
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=opts)
