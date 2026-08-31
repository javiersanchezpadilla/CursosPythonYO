""" ORDENAR Y AGRUPAR DATA FRAMES

    Vamos a colocar el archivo Top-Películas.cvs dentro del directorio
    de A01_Pandas ../A01_Pandas/ArchivosExternos/Top-Películas.csv.
    
    Realizar las siguiente operaciones:
    A)  Ordenar por el rating
    B)  Ordenar por rating y recaudación(M)
    C)  Agrupar por el genero de la pelicula y obtener el promedio del rating
    D)  Agrupar por año y en cada grupo sumar lo recaudado
"""
import pandas as pd 
from pathlib import Path

ruta = Path(__file__).resolve().parent.parent 
ruta = ruta / 'A01_Pandas/ArchivosExternos/Top-Películas.csv'

df = pd.read_csv(ruta)

# Odernando por un solo criterio
df_ordenado = df.sort_values(by='rating', ascending=False)
print(df_ordenado.head(3))

# Ordenando por mas de un criterio
df_ordenado = df.sort_values(by=['rating', 'recaudación(M)'], ascending=False)
print(df_ordenado.head(3))

# AGRUPAR
# Agrupar por el genero de la pelicula y obtener el promedio del rating
df_agrupado = df.groupby('género')['rating'].mean()
print(df_agrupado)

# Agrupar por año y en cada grupo sumar lo recaudado
df_agrupado2 = df.groupby('año')['recaudación(M)'].sum()
print(df_agrupado2)



