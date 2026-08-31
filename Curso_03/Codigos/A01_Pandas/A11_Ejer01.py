""" Ejercicio Operaciones Básicas con Series de Panda 1

    Crea dos series de pandas utilizando listas de Python.
    Puedes crear ambas series con los números de tu elección solamante
    asegurate de que la serie 1 y la serie 2 las almacenes en  variables
    nombradas: serie1 y serie2 respectivamente.

    Luego, suma ambas series y asigna el resultado a una variable llamada 
    serie_sumada. Imprime el resultado de serie_sumada.
"""
import pandas as pd 

serie1 = pd.Series([100, 200, 300, 400, 500, 600, 700])
serie2 = pd.Series([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7])

serie_sumada = serie1 + serie2
print(serie_sumada)

