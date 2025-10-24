Proyecto de Pruebas Automatizadas con Selenium
Este proyecto contiene pruebas automatizadas para el sitio SauceDemo(https://www.saucedemo.com/), utilizando Python, Selenium WebDriver y pytest.  
El objetivo es validar el funcionamiento de distintas secciones del sitio, como el login, el catálogo y el carrito de compras.

Propósito del proyecto

El propósito principal es automatizar casos de prueba funcionales del sitio de ejemplo SauceDemo, simulando la interacción de un usuario real en el navegador.  
Entre los escenarios cubiertos se incluyen:

Login.

Visualización del catálogo.

Validación de nombre, descripción y precio.

Agregado de productos al carrito.

Verificación del contenido del carrito.

Tecnologías utilizadas

Python 3.x

Selenium WebDriver

pytest

Google Chrome

ChromeDriver

Instalación y configuración

1-Clonar el repositorio

bash
git clone https://github.com/1Alexis1002/Pre-Entrega.git

cd -nombre del repositorio-

2-Instalar dependencias

pip install selenium pytest

pip install webdriver-manager

Ejecucion de pruebas

pytest -v

pytest tests/test_carrito.py -v para ejecutar un test especifico

pytest --html=report.html para ejecutar las pruebas y generar un reporte html