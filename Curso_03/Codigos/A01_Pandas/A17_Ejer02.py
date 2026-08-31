""" AGREGACIÓN DE SERIES EN PANDAS 1

    Crea una serie de Pandas a partir de la siguiente lista de 
    edades = [23, 30, 26, 27, 22, 24, 25, 28]
    
    Luego, utiliza las funciones adecuada para calcular los siguientes valores
    suma de edades, promedio, mediana, maximo , minimo, contar las edades
    
"""
import pandas as pd 

edades = [23, 30, 26, 27, 22, 24, 25, 28]

serie_edades = pd.Series(edades)

# resumen = serie_edades.agg(['sum', 'mean', 'median', 'mode', 'max', 'min', 'count'])
resumen = serie_edades.agg(['sum', 'mean', 'median', 'max', 'min', 'count'])
print(resumen)

