# 🐍 QA Python Mini Framework  

This project is a **QA mini-framework in Python** designed to demonstrate how to integrate **API, UI, and ETL processes** within the same ecosystem. It’s an ideal starting point for learning and showcasing skills in **test automation** and **data pipelines**.  

---

## 🚀 Key Features
- **API Testing** → modular HTTP client with `pytest`.  
- **UI Testing** → form automation and Google search using **Selenium WebDriver**.  
- **ETL (Extract, Transform, Load)** → practical examples of data extraction, transformation, and loading.  
- **Centralized configuration** with `config.py`.  
- **Scalable structure** → organized into modules (`api/`, `etl/`, `ui/`).  

---

## 📂 Project Structure

---

```
qa-python-miniframework/
│── src/
│ ├── api/ # API client and HTTP methods
│ ├── core/ # Configuration and schemas
│ ├── etl/ # Sample ETL scripts
│ └── ui/ # UI tests with Selenium
│
│── tests/
│ ├── api/ # API tests with pytest
│ └── ui/ # UI tests with pytest + Selenium
│
│── requirements.txt # Project dependencies
│── pytest.ini # Pytest configuration
```

---

## ⚙️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/youruser/qa-python-miniframework.git
   cd qa-python-miniframework

   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux / Mac
   .venv\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Running Tests

### 1. API Tests
```bash
pytest tests/api -v
```

### 2. UI Tests (Selenium)
```bash
pytest tests/ui -v
```

### 3. ETL Demo
```bash
python src/etl/ETL_demo.py
python src/etl/tiny-etl.py
```

---

## 🧩 Usage Example

### API Test
```python
def test_get_users(api_client):
    response = api_client.get("/users")
    assert response.status_code == 200
```

### UI Test
```python
def test_google_search(driver):
    driver.get("https://www.google.com")
    search_box = driver.find_element("name", "q")
    search_box.send_keys("QA Automation with Python")
    search_box.submit()
    assert "QA Automation" in driver.title
```

---

## 📌 Extending the Framework
- **New API endpoints → add functions in src/api/client.py.
- **New ETL pipelines → create scripts in src/etl/.
- **New UI tests → add them in tests/ui/ using Selenium.

---

## 🙌 Autor
Proyecto desarrollado por **Cristian Jáquez** como demostración de habilidades en **QA Automation, Python y ETL pipelines**.  
