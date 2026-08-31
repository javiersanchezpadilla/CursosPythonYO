""" Ejercicio Series en Pandas 2

    Crea una serie en Pandas a partir de la lista [10, 20, 30, 40] con índices 
    personalizados ['a', 'b', 'c', 'd']. Llama a esta serie serie_con_indices.
    Crea una variable llamada valor_c  donde almacenes el valor asociado al 
    índice 'c'

    Mostra el valor asociado al índice 'c'.
"""
import pandas as pd 

serie_con_indices = pd.Series([10, 20, 30, 40], ['a', 'b', 'c', 'd'])
valor_c = serie_con_indices['c']

print(serie_con_indices)
print(valor_c)
