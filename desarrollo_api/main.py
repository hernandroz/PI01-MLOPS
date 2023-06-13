# Importamos las dependencias necesarias:

from typing import Union
from fastapi import FastAPI
import pandas as pd

# Creamos una instancia de la aplicación FastAPI:

app = FastAPI()

#Cargamos los datos del csv:


df = pd.read_csv(r'C:\Users\Usuario\Desktop\desarrollo_api\movies_dataset_limpio.csv')


# Definimos las rutas y operaciones de la API mediante decoradores:

@app.get("cantidad_filmaciones_mes/{mes}")
def cantidad_filmaciones_mes( mes ): 
    # Se ingresa un mes en idioma Español. Debe devolver la cantidad de películas 
    # que fueron estrenadas en el mes consultado en la totalidad del dataset.
    # Ejemplo de retorno: "X cantidad de películas fueron estrenadas en el mes de X"
#    for d in df['release_date']:
#       count=0
#      if mes == d.strftime('%B'):
#         count = count+1
#respuesta = 'x'
    return {'mes': mes, 'cantidad': respuesta}

@app.get("cantidad_filmaciones_dia/{dia}")
def cantidad_filmaciones_dia( dia ): 
    # Se ingresa un día en idioma Español. Debe devolver la cantidad de películas que 
    # fueron estrenadas en día consultado en la totalidad del dataset.
    # Ejemplo de retorno: "X cantidad de películas fueron estrenadas en los días X"
    respuesta = 'x'
    return {'dia': dia, 'cantidad': respuesta}

@app.get("score_titulo/{titulo_de_la_filmacion}")
def score_titulo( titulo_de_la_filmacion ): 
    # Se ingresa el título de una filmación esperando como respuesta el título, el año 
    # de estreno y el score.
    # Ejemplo de retorno: "La película X fue estrenada en el año X con un score/popularidad de X"
    respuesta = 'x'
    return {'titulo_de_la_filmacion': titulo_de_la_filmacion, 'cantidad': respuesta}


@app.get("votos_titulo/{titulo_de_la_filmacion}")
def votos_titulo( titulo_de_la_filmacion ): 
    # Se ingresa el título de una filmación esperando como respuesta el título, la cantidad 
    # de votos y el valor promedio de las votaciones. La misma variable deberá de contar con 
    # al menos 2000 valoraciones, caso contrario, debemos contar con un mensaje avisando que 
    # no cumple esta condición y que por ende, no se devuelve ningun valor.
    # Ejemplo de retorno: "La película X fue estrenada en el año X. La misma cuenta con un 
    # total de X valoraciones, con un promedio de X"
    respuesta = 'x'
    return {'titulo_de_la_filmacion': titulo_de_la_filmacion, 'cantidad': respuesta}

@app.get("get_actor/{nombre_actor}")
def get_actor( nombre_actor ): 
    # Se ingresa el nombre de un actor que se encuentre dentro de un dataset debiendo devolver 
    # el éxito del mismo medido a través del retorno. Además, la cantidad de películas que en 
    # las que ha participado y el promedio de retorno. La definición no deberá considerar directores.
    # Ejemplo de retorno: El actor X ha participado de X cantidad de filmaciones, el mismo ha 
    # conseguido un retorno de X con un promedio de X por filmación
    respuesta = 'x'
    return {'nombre_actor': nombre_actor, 'cantidad': respuesta}

@app.get("get_director/{nombre_director}")
def get_director( nombre_director ): 
    # Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver 
    # el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada 
    # película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.
    respuesta = 'x'
    return {'nombre_director': nombre_director, 'cantidad': respuesta}