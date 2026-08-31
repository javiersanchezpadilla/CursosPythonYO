""" EJERCICIO TIPOS DE DATOS EN PANDAS 1

    Utilizando la biblioteca Pandas, crea un DataFrame llamado df_empleados 
    que contenga dos columnas: nombre y edad.
    La columna nombre debe contener los nombres de tres empleados: 
    'Ana', 'Luis' y 'Carlos'
    La columna edad debe contener las edades correspondientes: 30, 25 y 40
    Finalmente, muestra el DataFrame df_empleados utilizando la función print().

"""
import pandas as pd 

datos = {"nombre":['Ana', 'Luis', 'Carlos'], "edad":[30, 25, 40]}
print(datos)
print(type(datos))

df_empleados = pd.DataFrame(datos)
print("\nMostarndo los datos del data frame")
print(df_empleados)
print(type(df_empleados))

print("Mostrando los datos de cada serie")
print(df_empleados["nombre"])
print(df_empleados["edad"])
print(type(df_empleados["nombre"]))
print(type(df_empleados["edad"]))


