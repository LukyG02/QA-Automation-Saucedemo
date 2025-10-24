import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# Importamos el archivo login solo si queremos hacer el codigo de forma reutilizable y modular
#from utils.login import realizar_login

# Definimos la siguiente funcion global con el parametro (scope="function") para que ejecute cada test de manera independiente
@pytest.fixture(scope="function")
# Creamos una funcion driver() para inicializar el navegador y cerrarlo
def driver():
    # Inicia el navegador 
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    # Cierra el navegador
    driver.quit()

# Definimos otra funcion global
@pytest.fixture
# Creamos una funcion de login() con los parametros de las funciones driver() y wait()
# Ademas dentro de la funcion login() automatizamos el ingreso de credenciales de la pagina web utilizada

## En el caso de utilizar esta funcion de manera modular y reutilizable deberiamos dejar solo la funcion driver() como parametro
def login(driver, wait):
    # Realiza el login/ingreso antes de que algun tests lo necesite
    driver.get("https://www.saucedemo.com/")
    # Realizamos un print por consola para verificar que este en la pagina deseada
    print("Verificacion login")
    # Ingresamos las credenciales del login
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
    wait.until(EC.visibility_of_element_located((By.ID, "login-button")))
    # Verificamos que los datos ingresados sean correctos y le damos al boton "ingresar"
    driver.find_element(By.ID, "login-button").click()
    # Realizamos otro print por consola para verificar que se haya ingresado correctamente a la pagina
    print("Ingreso a la pagina")

    ## Si queremos utilizar una funcion modular y reutilizable, deberiamos ejecutar solo la linea de codigo de abajo 
    ## realizar_login(driver, "standard_user", "secret_sauce")

    # Esta linea de codigo deja abierta la pagina web por lo cual es indispensable ponerla al final de esta funcion
    yield driver


@pytest.fixture
# Creamos una funcion global para los tiempos de espera de los elementos de la pagina
def wait(driver):
    return WebDriverWait(driver, 10)