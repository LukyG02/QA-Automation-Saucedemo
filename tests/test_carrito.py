from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from conftest import login, wait

# Creamos una funcion para agregar los productos y le pasamos como parametros las funciones (login y wait)
def test_agregar_productos(login, wait):

    # Ingresamos a la pagina 
    driver = login

    # Realizamos un print por consola para verificar que estemos en el inventario
    print("Verificacion de productos")
    # Comprobamos que se encuentre el elemento y le creamos una variable numerica y en le agregamos un except por si el valor es 0
    try:
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
        carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        valor_inicial = int(carrito.text)
    except:
        valor_inicial = 0 
 
    #Imprimimos el valor inicial por consola
    print(f"Valor inicial del carrito: {valor_inicial}")

    # Comprobamos que se encuentre el producto y lo agregamos al carrito
    wait.until(EC.visibility_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack")))
    agregar_articulo = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    agregar_articulo.click()
    # Imprimimos un mensaje por consola que indique si el producto se añadio correctamente
    print(f"El producto fue añadido correctamente")

    # Verificamos el nuevo valor del contador
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    carrito_nuevo = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    valor_nuevo = int(carrito_nuevo.text)
    print(f"Valor nuevo del carrito: {valor_nuevo}")

    # Comprobamos que se encuentre el siguiente producto
    wait.until(EC.visibility_of_element_located((By.NAME, "add-to-cart-sauce-labs-bike-light")))
    agregar_articulo = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
    agregar_articulo.click()
    print(f"producto añadido correctamente")

    # Verificamos otra vez el valor del contador
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    carrito_nuevo = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    valor_nuevo = int(carrito_nuevo.text)
    print(f"Valor nuevo del carrito: {valor_nuevo}")

    # Ingresamos al carrito
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_link")))
    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    carrito.click()

    # Verificamos que los productos estén en el carrito
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name")))
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    print(productos)

    # Creamos una lista vacia
    productos_agregados = []

    # Creamos otra lista con un bucle sobre los productos almacenados anteriormente
    nombres = [p.text for p in productos]
    print(nombres)

    #Verificamos que todos los productos esten agregados
    assert "Sauce Labs Backpack" in nombres
    assert "Sauce Labs Bike Light" in nombres

    #Validamos que esten todos los productos esperados en el carrito mediante otro bucle 
    for producto in productos_agregados:
        assert producto in nombres, f"El producto {producto} no está en el carrito"