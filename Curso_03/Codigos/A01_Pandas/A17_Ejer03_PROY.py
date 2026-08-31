""" ANÁLISIS DE MEDALLAS OLÍMPICAS

    Objetivo
    --------

    Realizar un análisis exploratorio de datos (EDA) sobre un conjunto de 
    datos de medallas olimpicas utilizando Pandas. Este proyecto te permitirá 
    aplicar los conceptos aprendidos sobre Series, DataFrames, limpieza de 
    datos, operaciones básicas, filtrado y agregación en Pandas.

    Consigna
    --------
    Vas a trabajar con el conjunto de datos medallas.csv, que incluye 
    información sobre las medallas de oro, plata, bronce y el total obtenido 
    por cada pais en los Juegos Olimpicos.
    Vas a realizar una serie de tareas básicas, que te permitirán responder a 
    las preguntas de un cuestionario. 
    
    Las tareas que realizarás son:
    ------------------------------
    1.  Cargar los Datos: Importar los datos desde el archivo CSV a un 
        DataFrame de Pandas.
    2.  Exploración Inicial: Utilizar métodos básicos para explorar el tamaño, 
        las columnas y los tipos de datos del DataFrame.
    3.  Limpieza de Datos: Identificar y manejar valores faltantes o 
        incorrectos, especialmente en las columnas de medallas donde los 
        valores faltantes indican cero medallas
    4.  Análisis de Medallas de oro por País: Realiza las operaciones que sean 
        necesarias para identificar cuáles fueron los 3 países con más medallas 
        de oro en total (vas a necesitar investigar los métodos de dataframes 
        para encontrar cuál te permite ordenar los valores de mayor a menor o 
        viceversa) 
    5.  Análisis de Medallas Totales por Pais: Obtener un dataframe que contenga 
        sólo los paises que ganaron más de 10 medallas en total.

    Preguntas:
    ----------
    ¿Cuántas medallas en total tuvo el páis con más medallas conseguidas?
    ¿Cuál fue el segundo país con más medallas de oro?
    ¿Cuál es la desviación standard (std) de la columna "Total"?
    ¿Cuál era el tipo de datos original (Dtype) de la columna "Bronce"?

"""

import pandas as pd 
from pathlib import Path 


ruta = Path(__file__).resolve().parent
ruta = ruta / 'ArchivosExternos/medallas.csv'

# PASO 1. Importamos el archivo csv a un Data Frame de pandas
df = pd.read_csv(ruta)

# PASO 2. Exploración Inicial, Utilizar métodos básicos para explorar el 
#         tamaño de las columnas y los tipos de datos del DataFrame.
print('INFORMACIÓN GENERAL DEL DATA FRAME')
print(df.info())

renglones, columnas = df.shape
print(f'El data frame contiene {renglones} renglones y {columnas} columnas')

print('\nLA INFORMACIÓN GENERAL DEL DATA FRAME ES:')
print(df.describe())

print('\nVALORES NULOS')
print(df.isnull().sum())

print('\nMOSTRANDO LOS PRIMEROS TRES REGISTROS')
print(df.head(3))

print('\nMOSTRANDO LOS ÚLTIMOS TRES REGISTROS')
print(df.tail(3))

# PASO 3. Limpieza de datos (convertir los Nan por ceros)
print('\n\nLIMPIEZA DE DATOS:')
# FORMA 1
# criterio_relleno = {'Oro':0, 'Plata':0, 'Bronce':0}
# df_limpiados = df.fillna(criterio_relleno)
df_limpiados = df.fillna(0)
print(df_limpiados)
print('\n')
print(df_limpiados.isnull().sum())

# CORREGIR LOS TIPOS DE DATOS. NO tien caso que sean flotantes de 64
# cuando el total de medallas puede ser solo entero
df_limpiados['Oro'] = df_limpiados['Oro'].astype(int)
df_limpiados['Plata'] = df_limpiados['Plata'].astype(int)
df_limpiados['Bronce'] = df_limpiados['Bronce'].astype(int)


# PASO 4. Análisis de Medallas de oro por País: Realiza las operaciones que 
#         sean necesarias para identificar cuáles fueron los 3 países con más 
#         medallas de oro en total 
# Ordenamos el data frame por las medallas de oro
# RESPUESTA: Estados Unidos de America, China y JApon
df_ordenado = df_limpiados.sort_values(by='Oro',ascending=False)
print(df_ordenado.head(3))

# PASO 5. Análisis de Medallas Totales por Pais: Obtener un dataframe que 
#         contenga sólo los paises que ganaron más de 10 medallas en total
criterio = df_ordenado['Total'] > 10
df_mas_de_diez = df_ordenado[criterio]
print(df_mas_de_diez)

#  PREGUNTAS:
print('\n\nRESPUESTA AL CUESTIONARIO\n')
#  ¿Cuántas medallas en total tuvo el páis con más medallas conseguidas?
#  Respuesta 
print('Total de medallas del pais que consiguio mas triunfos')
print (df_ordenado.sort_values(by='Total', ascending=False).head(1))

# ¿Cuál fue el segundo país con más medallas de oro?
print('\nSegundo pais con mas medallas de oro')
pais_dos = df_ordenado.sort_values(by='Oro', ascending=False).head(2)
print(pais_dos.sort_values(by='Oro',ascending=True).head(1))

#  ¿Cuál es la desviación standard (std) de la columna "Total"?
print('\nLA DESVIACIÓN ESTANDAR DE LA COLUMNA TOTAL ES')
print(df_ordenado['Total'].std())

# ¿Cuál era el tipo de datos original (Dtype) de la columna "Bronce"?
print(type(df_ordenado['Bronce'][0]))
