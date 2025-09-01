# 🐍 QA Python Mini Framework  

Este proyecto es un **mini-framework de QA en Python** diseñado para mostrar cómo integrar pruebas de **API, UI y procesos ETL** en un mismo ecosistema. Es ideal como punto de partida para aprender y demostrar habilidades en **automatización de pruebas** y **pipelines de datos**.  

---

## 🚀 Características principales
- **API Testing** → cliente HTTP modular con `pytest`.  
- **UI Testing** → automatización de formularios y búsqueda en Google usando **Selenium WebDriver**.  
- **ETL (Extract, Transform, Load)** → ejemplos prácticos de extracción, transformación y carga de datos.  
- **Configuración centralizada** con `config.py`.  
- **Estructura escalable** → organizada en módulos (`api/`, `etl/`, `ui/`).  

---

## 📂 Estructura del proyecto
```
qa-python-miniframework/
│── src/
│   ├── api/              # Cliente API y métodos HTTP
│   ├── core/             # Configuración y esquemas
│   ├── etl/              # Scripts ETL de ejemplo
│   └── ui/               # Pruebas UI con Selenium
│
│── tests/
│   ├── api/              # Pruebas API con pytest
│   └── ui/               # Pruebas UI con pytest + Selenium
│
│── requirements.txt      # Dependencias del proyecto
│── pytest.ini            # Configuración de pytest
```

---

## ⚙️ Instalación
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tuusuario/qa-python-miniframework.git
   cd qa-python-miniframework
   ```

2. Crear y activar un entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux / Mac
   .venv\Scripts\activate      # Windows
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Ejecución de pruebas

### 1. Pruebas de API
```bash
pytest tests/api -v
```

### 2. Pruebas de UI (Selenium)
```bash
pytest tests/ui -v
```

### 3. ETL Demo
```bash
python src/etl/ETL_demo.py
python src/etl/tiny-etl.py
```

---

## 🧩 Ejemplo de uso

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

## 📌 Extender el framework
- **Nuevos endpoints API** → agregar funciones en `src/api/client.py`.  
- **Nuevos ETL pipelines** → crear scripts en `src/etl/`.  
- **Nuevas pruebas UI** → añadir en `tests/ui/` usando Selenium.  

---

## 🙌 Autor
Proyecto desarrollado por **Cristian Jáquez** como demostración de habilidades en **QA Automation, Python y ETL pipelines**.  
