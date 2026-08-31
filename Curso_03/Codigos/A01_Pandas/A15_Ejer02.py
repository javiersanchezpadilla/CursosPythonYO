""" Filtrado de Series en Pandas 2

    Dada una serie de Pandas que contiene los siguientes valores: 
    [18, 22, 7, 9, 15, 8], filtra y muestra solo aquellos valores que sean 
    pares.

    Primero, crea una serie de valores booleanos que represente la condición. 
    Nombra a esta variable como: condicion_valores_pares
    Luego aplica esta serie para filtrar los valores originales.
"""
import pandas as pd 

valores = [18, 22, 7, 9, 15, 8]
serie = pd.Series(valores)

# Creamos la condición
# OPCION 1 List Comprehension
# condicion_valores_pares = [True if valor % 2 == 0 else False for valor in valores]

# OPCION 2.
condicion_valores_pares = serie % 2 == 0

print(condicion_valores_pares)
print(serie[condicion_valores_pares])
