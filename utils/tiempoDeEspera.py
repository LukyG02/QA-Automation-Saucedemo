from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Creamos 2 funciones reutilizables para controlar los tiempos de espera de los elementos 

def esperar_elemento(driver, by, value, timeout=10):
    # Esperamos hasta que aparezca un elemento en el DOM
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

def esperar_y_hacer_click(driver, by, locator, timeout=10):
    # Esperamos a un elemento y luego hacemos click sobre el.
    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, locator))).click()