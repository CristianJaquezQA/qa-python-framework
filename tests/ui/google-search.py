from src.ui.driver import build_driver

def google_search():
    driver = build_driver()
    driver.get("https://www.google.com/search?q=")
    assert "Google" in driver.title
    driver.quit()

def facebook_search():
    driver = build_driver()
    driver.get("https://www.facebook.com/")
    assert "Facebook" in driver.title
    driver.quit()