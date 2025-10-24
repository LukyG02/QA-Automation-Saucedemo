from conftest import login

# Creamos una funcion para verificar que el ingreso de credenciales sea exitoso
def test_login_exitoso(login):

    # Ingresamos a la pagina
    driver = login

    # Verificamos que luego del login/ingreso, el navegador se haya redirigido hacia la URL del inventario
    assert "inventory" in driver.current_url