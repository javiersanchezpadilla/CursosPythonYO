""" Manejo de series

    Una serie es un arreglo de una sola dimensión

"""
import pandas as pd 
from pathlib import Path

ruta = Path(__file__).resolve().parent 
ruta = ruta / 'ArchivosExternos/Precipitaciones.csv'

df = pd.read_csv(ruta)

print(df.head())

# vamos a extraer del data frame la serie region
region = df['region']
print(region.head())

# Vamos a crear una serie a partir de una lista de datos
datos = [10, 20, 30, 40, 50, 60]
serie2 = pd.Series(datos)
print(type(serie2))
print(serie2)

# Personalización de los índices
mi_indice = ["a", "b", "c", "d", "e", "f"]
serie2 = pd.Series(datos, mi_indice)
print(serie2)

print(type(serie2))         # tipo de dato de serie2
print(type(serie2["d"]))    # tipo de dato del elemento "d" de serie2

# Convertir un diccionario a una serie
numeros = {"uno":1, "dos":2, "tres":3, "cuatro":4, "cinco":5, "diez":10}
serie3 = pd.Series(numeros)
print(serie3)
print(serie3["diez"])
print(serie3["tres"])
print(serie3["cinco"])
