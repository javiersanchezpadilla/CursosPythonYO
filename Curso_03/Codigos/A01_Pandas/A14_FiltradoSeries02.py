""" Filtrar series alfanumericas

    Se trata de filtrar series de texto, queremos buscar las frutas que
    contengan la letra 'm', recordar que no existe un método que permita
    buscar por el contenido de una serie
"""

import pandas as pd 

frutas = ["manzana", "melon", "pera", "uva", "sandia", "durazno"]
serie = pd.Series(frutas)
print(serie)

# BUSCAMOS AYUDA SOBRE EL COMANDO EN GOOGLE
# ------------------------------------------
# dentro de las series en pandas ¿existe un comando para buscar por contenido 
# de una cadena alfanumérica?

# en las series de pandas puedes usar el descriptor .str seguido de métodos 
# como .contains(), .match() o .findall() para buscar contenido dentro de 
# cadenas alfanuméricas de forma rápida y sencilla.
criterio = serie.str.contains('m')
print(criterio)

resultado = serie[criterio]
print(resultado)
