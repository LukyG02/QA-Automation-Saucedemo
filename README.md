# 🧪 Proyecto de Automatización QA con Selenium y Pytest

Este proyecto contiene pruebas automatizadas para validar el flujo principal de una aplicación web, incluyendo:

- ✅ Login de usuario  
- 🧩 Verificación de elementos de interfaz  
- 🛒 Agregado de productos al carrito  
- 💳 Compra completa  

---

## 🧠 SauceDemo Automation Testing (Pytest + Selenium)

Proyecto de práctica de automatización de pruebas UI utilizando **Python**, **Pytest** y **Selenium WebDriver**.  
Se automatizan flujos de login, navegación, carrito de compras y finalización de compra en el sitio de demostración:  
👉 [SauceDemo](https://www.saucedemo.com/)

---

## 📂 Estructura del Proyecto

- **`test-env/`** → Entorno virtual de desarrollo.  
- **`tests/`** → Casos de prueba organizados por funcionalidad.  
- **`utils/`** → Funciones auxiliares reutilizables.  
- **`reports/`** → Reportes HTML generados después de cada ejecución.  
- **`conftest.py`** → Fixtures principales (driver, login, esperas, etc.).  
- **`requirements.txt`** → Lista de dependencias del entorno.

---

## ⚙️ Tecnologías Utilizadas

- 🐍 **Python**  
- 🧪 **Pytest**  
- 🌐 **Selenium WebDriver**  
- ⚙️ **WebDriver Manager**  

---

## ▶️ Instalación y Ejecución

### 1️⃣ Instalar dependencias
**Consola**
pip install -r requirements.txt

### 2️⃣ Ejecutar pruebas
**Pruebas Conjuntas**
pytest -v run_tests.py
**Pruebas individuales**
pytest -v test/**nombredelaprueba**.py

### 3️⃣ Ver prints y seguimiento detallado
**El modificador -s permite ver los print() del código durante la ejecución (recomendado para depuración).**
pytest -v -s run_tests.py

## ▶️ Ejecución de reportes
# Ejecutamos el archivo run_tests.py de la siguiente forma
**Ejecuta las pruebas y te genera un archivo html con el reporte de los tests**
pytest -v run_tests.py

**Si queremos ver por consola los prints que hay dentro del codigo y hacer un seguimiento mas especifico agregamos el comando (-s) luego del comando (-v). (RECOMENDABLE)**
pytest -v -s run_tests.py

## 🚀 Estructura del proyecto

## 🧠 Casos de Prueba Automatizados
🔹 test_login.py
- Validar login exitoso.
- Verificar redirección a la página de inventario.

🔹 test_navegacion.py
- Verificar título correcto en la página de inventario.
- Confirmar presencia de menú, filtros y productos visibles.

🔹 test_carrito.py
- Verificar que los productos se agregan correctamente.
- Validar que el contador del carrito se actualiza.

🔹 test_compra.py
- Completar el flujo de compra.
- Validar que se muestre el mensaje de confirmación.

## 🧩 Estructura de Fixtures (conftest.py)
El archivo conftest.py contiene fixtures globales para reutilizar en todos los tests:
- driver → inicializa y cierra el navegador.
- wait → controla esperas explícitas.
- login → realiza el inicio de sesión antes de cada test.

## 🧰 Funciones Auxiliares (utils/)
La carpeta utils/ contiene funciones reutilizables, como:
- Login automatizado
- Métodos para interactuar con elementos
- Validaciones comunes
- Generación de datos de prueba
Esto mejora la organización y evita duplicar código.

## 📄 Reportes de Ejecución
Cada vez que se ejecuta run_tests.py, se genera un reporte HTML dentro de la carpeta reports/, con el resumen de resultados:
- Pruebas pasadas y fallidas
- Logs de ejecución

## 🧠 Aprendizajes y Buenas Prácticas Aplicadas
- Organización modular del proyecto.
- Uso de fixtures con distintos scope.
- Implementación de esperas explícitas con WebDriverWait.
- Validaciones con assert.
- Generación automática de reportes HTML.
- Control de versiones con .gitignore y GitHub.

---

## 👨‍💻 Autor

**Lucas Hernan Gonzalez**  
Proyecto académico del curso de **Testing QA Automation**.