""" Ejercicio Operaciones Básicas con Series de Panda 2

    Dada una serie de pandas llamada serie_numerica que contienga los números 
    de tu preferencia.
    Realiza las siguientes operaciones matemáticas y guarda los resultados en 
    variables separadas:

    Multiplica serie_numerica por 2 y guarda el resultado en serie_doble.
    Divide serie_numerica por 10 y guarda el resultado en serie_dividida.
    Imprime los resultados de serie_doble y serie_dividida.
    Raiz mostrar la raiz cuadrada de los items 1, 3, 5
"""
import pandas as pd 
from math import * 

datos = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
serie_numerica = pd.Series(datos)

serie_doble = serie_numerica * 2
serie_dividida = serie_numerica / 2 

print('Serie Original')
print(serie_numerica)
print('\nSerie doble') 
print(serie_doble)
print('\nSerie dividida') 
print(serie_dividida)

print("\n\nRaiz cuadrada")
print("item 1", serie_numerica[0] ** 0.5)
print("item 3", serie_numerica[3] ** 0.5)
print("item 5", serie_numerica[5] ** 0.5)

print("\n\nRaiz cuadrada metodo sqrt()")
print("item 1", sqrt(serie_numerica[0]))
print("item 3", sqrt(serie_numerica[3]))
print("item 5", sqrt(serie_numerica[5]))
