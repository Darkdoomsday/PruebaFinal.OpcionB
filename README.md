# PruebaFinal.OpcionB
## Prueba Final de Ciberseguridad - 2023B - Opción B
### Esta práctica consistirá en tomar información de una fuente de datos en línea, para lo cual, hemos seleccionado juegos lúdicos y cuya segmentación estará orientada a juegos de mesa. El link de la página con la que trabajará, es la siguiente: [Juegos de la Mesa Redonda](https://juegosdelamesaredonda.com).

**Requisitos Previos**

1. Un entorno de desarrollo (IDE) como VSCode o Pycharm (Para esta práctica se hará uso de Pycharm).
2. Crear una cuenta en [MongoDB](https://cloud.mongodb.com).
3. Navegador Web (Firefox, Google Chrome), usaremos Google Chrome para la práctica.
4. Instalar un Web Driver acorde a la versión del navegador web [Firefox](https://w3c.github.io/webdriver/), [Chrome](https://chromedriver.chromium.org/downloads).
5. Instalar Selenium por medio de Pycharm.

**Esquema de la Práctica**

![image](https://github.com/Darkdoomsday/PruebaFinal.OpcionB/assets/140026173/cee65bf7-7993-4c54-ab58-d99cde1196a5)

**Funcionamiento**
1. Con ayuda de las herramientas Selenium, Web Driver (Chrome) y Python (IDE Pycharm), se desarrollará el código necesario para acceder de manera automática al sitio web que se desea extraer la información.
2. Una vez en el sitio web, se ha desarrollado el poder buscar el objeto "Cartas", con el cual, se desplegará toda la información del sitio que haga coincidencia con esa búsqueda.
3. Una vez desplegada la información, será extraída y visualizada en el terminal de Pycharm.
4. Una vez extraída la información, se realizará la inserción en la base de datos MongoDB en formato JSON (datos estructurados en forma de texto).
5. En MongoDB, se deberá visualizará la información insertada según lo obtenido en la página web.
6. Se realizará la lectura de los datos en la base de datos MongoDB, sin embargo, esto se encontrará explicado en otro repositorio [Lectura de Datos](https://github.com/Darkdoomsday/PruebaFinal.OpB.WebService).

**Links de Código**

Los link del código para poder realizar la práctica sería el siguiente:

1. Acceso a página web, búsqueda y extración de información [main](https://github.com/Darkdoomsday/PruebaFinal.OpcionB/blob/main/main.py).
2. Clase de conexión e inserción de información a la base de MongoDB [db](https://github.com/Darkdoomsday/PruebaFinal.OpcionB/blob/main/db.py).
3. Librerías utilizadas de selenium y [requirements](https://github.com/Darkdoomsday/PruebaFinal.OpcionB/blob/main/requirements.txt).
4. Documento con credenciales de conexión a DB (no públicas (.env)).

**Novedades en el Camino**
