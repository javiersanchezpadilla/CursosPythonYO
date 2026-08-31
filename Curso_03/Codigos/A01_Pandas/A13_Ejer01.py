""" Ejercicio Limpieza de Datos en Pandas 1

    Dada una tabla (Diccionario) de ventas que contiene información sobre 
    productos vendidos, incluyendo ID, Producto, Cantidad y Precio,

        data = {
            'ID': [1, 2, 3, 4, 5],
            'Producto': ['Prod A', 'Prod B', None, 'Prod D', 'Prod E'],
            'Cantidad': [10, 20, 30, None, 50],
            'Precio': [100, 200, 300, 400, None]
        }

    A)  Escribe un código en Python usando Pandas para contar los valores nulos 
        por columnas.
"""

import pandas as pd 

data = { 'ID': [1, 2, 3, 4, 5],
         'Producto': ['Prod A', 'Prod B', None, 'Prod D', 'Prod E'],
         'Cantidad': [10, 20, 30, None, 50],
         'Precio': [100, 200, 300, 400, None] }

df = pd.DataFrame(data)
print(df.isnull().sum())
