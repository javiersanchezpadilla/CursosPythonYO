""" Ejercicio Limpieza de Datos en Pandas 2

    El conjunto de datos proporcionado tiene algunas entradas duplicadas.

        data = {
            'ID': [1, 2, 3, 4, 1],
            'Producto': ['Prod A', 'Prod B', 'Prod C', 'Prod D', 'Prod A'],
            'Cantidad': [10, 20, 30, 40, 50],
            'Precio': [100, 200, 300, 400, 100]
        }

    Escribe un script en Python usando Pandas para eliminar los registros con 
    ID duplicados, utilizando la columna ID como referencia para identificar 
    los duplicados. Almacena el resultado en una variable llamada: 
    df_sin_duplicados.
"""
import pandas as pd

data = {
    'ID': [1, 2, 3, 4, 1],
    'Producto': ['Prod A', 'Prod B', 'Prod C', 'Prod D', 'Prod A'],
    'Cantidad': [10, 20, 30, 40, 50],
    'Precio': [100, 200, 300, 400, 100]
}
#    ID Producto  Cantidad  Precio
# 0   1   Prod A        10     100
# 1   2   Prod B        20     200
# 2   3   Prod C        30     300
# 3   4   Prod D        40     400
# 4   1   Prod A        50     100
df = pd.DataFrame(data)


# Eliminamos aquellos donde ID sea duplicado
#    ID Producto  Cantidad  Precio
# 0   1   Prod A        10     100
# 1   2   Prod B        20     200
# 2   3   Prod C        30     300
# 3   4   Prod D        40     400
df_sin_duplicados = df.drop_duplicates(subset="ID")
print(df)
print("\n\nSin duplicados")
print(df_sin_duplicados)
