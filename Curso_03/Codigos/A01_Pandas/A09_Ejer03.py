""" Ejercicio Series en Pandas 3

    Utiliza el diccionario {'a': 30, 'b': 70, 'c': 160, 'd': 50} para crear 
    una serie en Pandas, la cual llamarás serie_desde_diccionario.
    Luego, accede a los valores asociados a los índices 'a' y 'd', sumándolos. 
    Almacena esta suma en la variable suma_ad
    Muestra los resultados.
"""

import pandas as pd 

serie_desde_diccionario = pd.Series({'a': 30, 'b': 70, 'c': 160, 'd': 50})
suma_ad = serie_desde_diccionario['a'] + serie_desde_diccionario['d']

print(serie_desde_diccionario)
print(suma_ad)
