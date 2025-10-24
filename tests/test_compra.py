## Si queremos reutilizar las funciones del archivo "tiempoDeEspera"
## from utils.tiempoDeEspera import esperar_elemento, esperar_y_hacer_click
from conftest import login, wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Creamos una funcion para simular y testear el ingreso de datos para la compra de productos en la pagina
def test_de_compra(login, wait):

    # Ingresamos a la pagina
    driver = login

    # Ingresamos al carrito de compra
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Le damos al boton de "continuar"
    wait.until(EC.visibility_of_element_located((By.NAME, "checkout")))
    driver.find_element(By.NAME,"checkout").click()

    # Ingresamos el nombre del usuario
    nombre = wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
    nombre.send_keys("Lautaro")

    # Ingresamos el apellido del usuario
    apellido = wait.until(EC.visibility_of_element_located((By.ID, "last-name")))
    apellido.send_keys("Ibarra")

    # Ingresamos el codigo postal del usuario
    codigo = wait.until(EC.visibility_of_element_located((By.ID, "postal-code")))
    codigo.send_keys("4356")

    # Verificamos que los datos ingresados sean correctos y le damos al boton de "continuar"
    wait.until(EC.element_to_be_clickable((By.ID, "continue")))
    driver.find_element(By.NAME,"continue").click()

    # Verificamos que los datos de compra sean correctos y le damos al boton de "finalizar compra"
    wait.until(EC.visibility_of_element_located((By.ID, "finish")))
    driver.find_element(By.ID,"finish").click()

    # Verificamos que la compra se haya hecho correctamente y le damos al boton de "volver al inicio"
    wait.until(EC.visibility_of_element_located((By.ID, "back-to-products")))
    driver.find_element(By.ID,"back-to-products").click()