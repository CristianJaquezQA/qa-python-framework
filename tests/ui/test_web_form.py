import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.ui
def test_web_form_submit(driver):
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    wait = WebDriverWait(driver, 10)

    input_box = wait.until(EC.visibility_of_element_located((By.NAME, "my-text")))
    input_box.clear()
    input_box.send_keys("Hola Cristian")

    dropdown = Select(wait.until(EC.element_to_be_clickable((By.NAME, "my-select"))))
    dropdown.select_by_visible_text("Two")

    # Click en botón
    btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button")))
    btn.click()

    # Verificamos el mensaje
    msg = wait.until(EC.visibility_of_element_located((By.ID, "message")))
    assert "Received!" in msg.text
