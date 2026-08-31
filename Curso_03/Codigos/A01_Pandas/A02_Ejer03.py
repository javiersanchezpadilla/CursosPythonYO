""" EJERCICIO TIPOS DE DATOS EN PANDAS 3

    Dado el DataFrame df_empleados creado en el ejercicio anterior:
    La columna nombre debe contener los nombres de tres empleados: 
    'Ana', 'Luis' y 'Carlos'
    La columna edad debe contener las edades correspondientes: 30, 25 y 40
    Para explorar sus atributos principales: shape, columns, y index.
    Utilizando las siguientes variables respectivamente: 
    shape_df, columns_df, index_df 
    Imprime los resultados de cada exploración para demostrar tu comprensión 
    de la estructura de los DataFrames y las Series en Pandas.
    El resultado esperado es el siguiente:
    (3, 2)
    Index['nombre, 'edad'], dtype='object'
    RangeIndex(start=0, stop=3, step=1)
    
    En Pandas, estos tres atributos se conocen como metadatos o propiedades 
    estructurales de un DataFrame o Serie.
    A diferencia de los métodos de Pandas (como .describe() o .head()), no 
    llevan paréntesis () al final porque no ejecutan una función, simplemente 
    leen la estructura de la tabla existente.

    1. .shape (La Forma o Dimensiones)
    ----------------------------------
    Despliega una tupla de números enteros que representa las dimensiones del 
    DataFrame en el formato (filas, columnas).
    Uso principal: Conocer rápidamente el tamaño total de tu conjunto de datos 
    (cuántos registros y cuántas variables tienes).
    
    2. .columns (Las Columnas)
    --------------------------
    Despliega un objeto especial de Pandas llamado Index que contiene todos 
    los nombres de las columnas del DataFrame.
    Uso principal: Inspeccionar las variables de tu tabla, verificar el nombre 
    exacto de las columnas o iterar sobre ellas.
    Si necesitas convertir este resultado en una lista normal de Python para 
    trabajar con ella, simplemente la envuelves en list():
    
    3. .index (El Índice de las Filas)
    ----------------------------------
    Despliega la estructura del índice (las etiquetas o números de posición de 
    las filas).
    Por defecto, cuando creas o lees un DataFrame sin definir un índice 
    explícito, Pandas genera un índice numérico secuencial que empieza en 0. 
    Por eso despliega un objeto RangeIndex. (ini, final(no inclusivo), paso)
    Uso principal: Identificar cómo están etiquetadas las filas o ver el rango 
    del identificador.
"""

import pandas as pd 

datos = {'nombre': ['Ana', 'Luis', 'Carlos', 'Luis'], 'edad': [30, 25, 40,  50]}
df_empleados = pd.DataFrame(datos)

shape_df = df_empleados.shape
columns_df = df_empleados.columns
index_df = df_empleados.index

print('Valor de Shape:', shape_df, '(filas y columnas)')
print('Total de filas', df_empleados.shape[0])
print('Total columnas', df_empleados.shape[1])
print('Valor de columns:', columns_df)
print('Valor de index:', index_df)      # rangeindex( ini, fin(no inclusivo), paso)
