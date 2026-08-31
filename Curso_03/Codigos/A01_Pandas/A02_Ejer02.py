""" EJERCICIO TIPOS DE DATOS EN PANDAS 2

    Dado el DataFrame df_empleados creado en el ejercicio anterior:
    La columna nombre debe contener los nombres de tres empleados: 
    'Ana', 'Luis' y 'Carlos'
    La columna edad debe contener las edades correspondientes: 30, 25 y 40
    Utiliza el método adecuado para seleccionar solo la columna edad y 
    almacénala en una variable llamada edades.
    Luego, muestra el contenido de edades utilizando la función print().
    Asegúrate de demostrar que el tipo de dato de edades es una Serie de 
    Pandas. Utilizando la función type().
"""
import pandas as pd 

datos = {'nombre': ['Ana', 'Luis', 'Carlos'], 'edad': [30, 25, 40]}
df_empleados = pd.DataFrame(datos)

edades = df_empleados.edad
edades2 = df_empleados['edad']  # <-- Esta es la mas sencilla de recordar
print(edades)
print(edades2)
print(type(edades))
print(type(edades2))
