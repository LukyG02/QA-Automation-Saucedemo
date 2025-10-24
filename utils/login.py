from selenium.webdriver.common.by import By

# Creamos una funcion reutilizable para el login de manera "modular"
def realizar_login(driver, username, password):
    # Realizamos el login de la pagina
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    print("Ingreso a la pagina")