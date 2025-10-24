import pytest

# Creamos una variable y almacenamos/indicamos el orden de ejecucion de los tests 
test_files = [
    "tests/test_login.py",
    "tests/test_navegacion.py",
    "tests/test_carrito.py",
    "tests/test_compra.py"
]

# Luego creamos otra variable y almacenamos la variable de los tests(anteriormente creada) y agregamos el siguiente comando
pytest_args = test_files + ["--html=reports/reporte.html", "--self-contained-html","-v", "-s"]

# Con esta linea de codigo nos permite ejecutar todas las pruebas solo ejecutando este archivo.                           
pytest.main(pytest_args)