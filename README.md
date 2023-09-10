# Prueba Final de Ciberseguridad - 2023B - Opción B
## Esta práctica consistirá en tomar información de una fuente de datos en línea (página web), para lo cual, hemos seleccionado juegos lúdicos y cuya segmentación estará orientada a juegos de mesa.

+ ### El link de la página con la que trabajará, será la siguiente: [Juegos de la Mesa Redonda](https://juegosdelamesaredonda.com).

![image](https://github.com/Darkdoomsday/PruebaFinal.OpcionB/assets/140026173/f30f083f-f48d-4be6-a404-15859aedb745)

**Requisitos Previos**

1. Un entorno de desarrollo (IDE) como VSCode o Pycharm (Para esta práctica se hará uso de Pycharm).
2. Crear una cuenta en [MongoDB](https://cloud.mongodb.com).
3. Navegador Web (Firefox, Google Chrome), usaremos Google Chrome para la práctica.
4. Instalar un Web Driver acorde a la versión del navegador web [Firefox](https://w3c.github.io/webdriver/), [Chrome](https://chromedriver.chromium.org/downloads).
5. Instalar Selenium por medio de Pycharm.

***ESQUEMA DE LA PRÁCTICA***

![image](https://github.com/Darkdoomsday/PruebaFinal.OpcionB/assets/140026173/cee65bf7-7993-4c54-ab58-d99cde1196a5)

***FUNCIONAMIENTO***
1. Con ayuda de las herramientas Selenium, Web Driver (Chrome) y Python (IDE Pycharm), se desarrollará el código necesario para acceder de manera automática al sitio web que se desea extraer la información.
2. Una vez en el sitio web, se ha desarrollado el poder buscar el objeto "Cartas", con el cual, se desplegará toda la información del sitio que haga coincidencia con esa búsqueda.
3. Una vez desplegada la información, será extraída y visualizada en el terminal de Pycharm.
4. Una vez extraída la información, se realizará la inserción en la base de datos MongoDB en formato JSON (datos estructurados en forma de texto).
5. En MongoDB, se deberá visualizará la información insertada según lo obtenido en la página web.
6. Se realizará la lectura de los datos en la base de datos MongoDB, sin embargo, esto se encontrará explicado en otro repositorio [Lectura de Datos](https://github.com/Darkdoomsday/PruebaFinal.OpB.WebService).

***LINKS DE CÓDIGO***

Los link del código para poder realizar la práctica sería el siguiente:

1. Archivo principal que permite acceso a página web, búsqueda y extración de información [main](https://github.com/Darkdoomsday/PruebaFinal.OpcionB/blob/main/main.py).
2. Archivo con la clase de conexión e inserción de información a la base de MongoDB [db](https://github.com/Darkdoomsday/PruebaFinal.OpcionB/blob/main/db.py).
3. Librerías utilizadas de selenium y MongoDB [requirements](https://github.com/Darkdoomsday/PruebaFinal.OpcionB/blob/main/requirements.txt).
4. Documento con credenciales de conexión a DB (no públicas (.env)).

***NOVEDADES PRESENTADAS***

Las novedades encontradas en el camino fue, en un inicio no se podía extraer los datos de la pseudo clase li:nth-child() dentro del código como elemento independiente,es decir, en la parte del código donde se extraía cada elemento antes de la impresión y a la función de inserción de la clase db.py, para su almacenamiento. Luego de varios intentos encontré la solución, en la sección donde extraía todo el contenedor, es decir, la parte de la página web que contenía todos los "child", coloqué el código "li:nth-child(n)", con el cuál y donde **n**, me permitió extraer todos los elementos según lo requerido.

+ #### **PROBLEMA**

![image](https://github.com/Darkdoomsday/PruebaFinal.OpcionB/assets/140026173/dd484a80-b0db-4139-b73b-8d315fed4bad)

Cabe indicar que incluso, al retirar el código "li:nth-child(*)", me entregaba únicamente el primer registro.

![image](https://github.com/Darkdoomsday/PruebaFinal.OpcionB/assets/140026173/92fca084-50a8-4451-99ec-613d89c4f1d5)

+ #### **SOLUCIÓN**

![image](https://github.com/Darkdoomsday/PruebaFinal.OpcionB/assets/140026173/333665bd-3291-4490-89ae-44d4cae4e2c2)

```py
articles = driver.find_elements(By.CSS_SELECTOR, "#center_column > ul > li:nth-child(n) > div")

mongodb = MongoDriver()

for card in articles:
    try:
        #image = card.find_element(By.CSS_SELECTOR, "div > div > div.left-block2.col-xs-4.col-xs-4.col-md-3 > div > a > img").image
        title = card.find_element(By.CSS_SELECTOR, "div > div > div.center-block2.col-xs-4.col-xs-7.col-md-6 > h3 > a").text
        description = card.find_element(By.CSS_SELECTOR, "div > div > div.center-block2.col-xs-4.col-xs-7.col-md-6 > p").text
        price = card.find_element(By.CSS_SELECTOR, "div > div > div.right-block2.col-xs-4.col-xs-7.col-md-3 > div > div.content_price.col-xs-12.col-md-12 > span").text
        print(title)
        print(description)
        print(f"{price}")

        juegos = {
            "Título": title,
            "Descripción": description,
            "Precio": price
        }



        mongodb.insert_record(record=juegos, username="cartas")

        print("++++++++++++++++++++++++++++++++")
    except Exception as e:
        print(e)
        print("++++++++++++++++++++++++++++++++")
```

![image](https://github.com/Darkdoomsday/PruebaFinal.OpcionB/assets/140026173/c54d485d-1a65-4bb0-8f9e-d085126636b4)

![image](https://github.com/Darkdoomsday/PruebaFinal.OpcionB/assets/140026173/6c9eba7e-e4d4-4ee1-a00e-b47e6a91f30a)

***CONCLUSIÓN***

La práctica ha sido concluida con éxito, sin embargo, es importante el seguir investigando y practicando con otros sitios web, dado que, la extracción de información o web scrapping como se lo denomina, es diferente en cada sitio. Esto debido a la construcción, lenguaje de programación y composición que tiene cada página propiamente hablando, por tanto, el código para la extracción de información puede variar según sea el caso.
