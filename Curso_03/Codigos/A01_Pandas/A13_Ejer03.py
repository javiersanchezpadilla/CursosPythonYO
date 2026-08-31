""" Ejercicio Limpieza de Datos en Pandas 3

    Tu tabla de ventas, la columna 'Precio' tiene algunos valores nulos.

        data = {
            'ID': [1, 2, 3, 4],
            'Producto': ['Prod A', 'Prod B', 'Prod C', 'Prod D'],
            'Cantidad': [10, 20, 30, 40],
            'Precio': [100, None, 300, None]
        }
        
    Escribe un código en Python usando Pandas para reemplazar los valores nulos 
    en la columna Precio por el promedio de los precios no nulos de esa columna


"""
import pandas as pd 

data = { 'ID': [1, 2, 3, 4],
         'Producto': ['Prod A', 'Prod B', 'Prod C', 'Prod D'],
         'Cantidad': [10, 20, 30, 40],
         'Precio': [100, None, 300, None] }

df = pd.DataFrame(data)
#    ID Producto  Cantidad  Precio
# 0   1   Prod A        10   100.0
# 1   2   Prod B        20     NaN
# 2   3   Prod C        30   300.0
# 3   4   Prod D        40     NaN
print(df)

print("\n\nDos doritos después:")
#    ID Producto  Cantidad  Precio
# 0   1   Prod A        10   100.0
# 1   2   Prod B        20   200.0  <-- (100 + 300) / 2 = 200
# 2   3   Prod C        30   300.0
# 3   4   Prod D        40   200.0  <-- (100 + 300) / 2 = 200
criterio = {"Precio":df["Precio"].mean()}
df = df.fillna(criterio)
print(df)