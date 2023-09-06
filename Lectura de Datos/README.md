# Prueba Final de Ciberseguridad - 2023B - Opción B - Lectura de Datos
## Este código fue utilizado para la extracción de información (datos) que se encontraba en una base de datos en MongosDB del ejercicio antes mencionado.

### ***ESQUEMA***

![image](https://github.com/Darkdoomsday/PruebaFinal.OpcionB/assets/140026173/48c58580-888d-4798-b545-b0194ba40693)


**La base de datos ubicada en MongoDB, contiene la siguiente información:**

![image](https://github.com/Darkdoomsday/PruebaFinal.OpcionB/assets/140026173/3954c0c6-412f-46ce-8328-ab3495ccc801)

##### ***Donde;***

+ ##### **NOMBRE DE BASE DE DATOS:** db_eig
+ ##### **COLECCIÓN:** cartas_juegosdemesa

### ***CÓDIGO***

Para la conexión y lectura de la información de la base de datos, se empleó el siguiente código.

```py

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv('MONGO_USER')
password = os.getenv('MONGO_PASSWORD')
hostname = os.getenv('MONGO_HOSTNAME')

uri = f"mongodb+srv://{user}:{password}@{hostname}/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


def read():
    try:
        lectura = client.get_database('db_eig').get_collection('cartas_juegosdemesa').find()
        for file in lectura:
            print(file)
    except Exception as e:
        print(e)


read()

```

### ***RESULTADO***

![image](https://github.com/Darkdoomsday/PruebaFinal.OpcionB/assets/140026173/0e987bb3-d277-4005-a18f-fac1d9ed1b24)

### ***CONCLUSIÓN***

Como se puede apreciar, se logró obtener la información de la base de datos, donde, se consideró la colección "juegodecartas" para poderla importar.

