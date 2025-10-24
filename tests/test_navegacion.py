## Importamos las funciones del archivo "tiempoDeEspera", solo si queremos reutilizar sus funciones 
## from utils.tiempoDeEspera import esperar_elemento , esperar_y_hacer_click
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from conftest import login, wait

## En el caso de reutilizar las funciones de tiempoDeEspera solo ingresar como parametro login
def test_navegacion(login, wait):

    # Ingreso a la pagina
    driver = login

    # Verificamos el titulo de la pagina del inventario
    titulo = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "app_logo"))).text

    # Corroboramos que el titulo deseado es el correcto 
    assert titulo == "Swag Labs", f"El titulo esperado era Swag Labs pero se encontro: {titulo}"

    # Verificamos por consola si el titulo es correcto
    print(f"Titulo correcto: {titulo}")

    # Verificamos todos los productos que se encuentran en la pagina de inventario
    wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0, "No se encontraron productos disponibles"

    # Realizamos un print para verificar la cantidad de productos encontrados
    print(f"La cantidad de productos encontrados son {len(productos)}")

    # Comprobamos y almacenamos en una variable los elementos claves de la pagina
    menu = driver.find_elements(By.ID, "react-burger-menu-btn")
    filtro = driver.find_elements(By.CLASS_NAME, "product_sort_container")
    carrito = driver.find_elements(By.CLASS_NAME, "shopping_cart_link")

    ## Si queremos reutilizar la funcion "esperar_elemento" y hacer el codigo de forma más modular.
    ## menu = esperar_elemento(driver, By.ID, "react-burger-menu-btn")
    ## filtro = esperar_elemento(driver, By.ID, "product_sort_container")
    ## carrito = esperar_elemento(driver, By.ID, "shopping_cart_link")

    # Verificamos si los elementos claves de la pagina se encuentran
    assert menu, "El menu no se encuentra"
    assert filtro, "El filtro no se encuentra"
    assert carrito, "El carrito no se encuentra"

    # Realizamos un print para corroborar que todos los elementos claves fueron encontrados
    print("Todos los elementos claves de la interfaz fueron encontrados")