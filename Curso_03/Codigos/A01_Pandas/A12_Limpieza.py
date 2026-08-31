""" Limpieza de datos

    El analisis rápido del data frame me dará como resultado
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 4 entries, 0 to 3                   <-- Tiene 4 entradas
    Data columns (total 3 columns):                 <-- 3 columnas
    #   Column            Non-Null Count  Dtype  
    ---  ------            --------------  -----  
    0   Id_producto       4 non-null      int64     <-- 4 valores no null
    1   Cantidad_vendida  3 non-null      float64   <-- 3 no null 1 null
    2   Precio            3 non-null      float64   <-- 3 no null 1 null
    dtypes: float64(2), int64(1)        <-- contien datos flotantes y enteros
    memory usage: 228.0 bytes
    None

"""
import pandas as pd 

valores = {"Id_producto":[1001, 1002, 1003, 1003],
           "Cantidad_vendida":[30, None, 25, 25],
           "Precio":[20.5, 15.0, None, 22.5]}

df = pd.DataFrame(valores)
print(df)

# REalizamos un analisis rápido de mi data frame
print(df.info())

# identificamos los valores nulos de cada columa
#    Id_producto  Cantidad_vendida  Precio
# 0        False             False   False
# 1        False              True   False  <-- contiene 1 valor null
# 2        False             False    True  <-- contiene 1 valor null
# 3        False             False   False
print(df.isnull())

# acumulamos los valores nulos por columna
# Id_producto         0
# Cantidad_vendida    1
# Precio              1
# dtype: int64
print(df.isnull().sum())

# Tenemos que decidir que vamos a hacer con los valores nulos, esto está 
# en funcion del caso de estudio, en algunos casos podemos eliminar los registros
# reemplazarlos por ceros, reemplazarlos por su valor promedio, por una palabra

# Criterio 1. eliminar los registros con valores nulos
#    Id_producto  Cantidad_vendida  Precio
# 0         1001              30.0    20.5
# 3         1003              25.0    22.5
df_eliminados = df.dropna()
print(df_eliminados)

# Criterio 2. rellenar los valores nulos de la columna cantidad_vendida con zeros
# rellenar las columnas de precio con el promedio de los precios de la serie
#    Id_producto  Cantidad_vendida     Precio
# 0         1001              30.0  20.500000
# 1         1002               0.0  15.000000   <-- Se cambio a cero el valor
# 2         1003              25.0  19.333333   <-- Se cambio por valor promedio
# 3         1003              25.0  22.500000
# creamos un diccionario con los criterios a considerar
valores_nuevos = {"Cantidad_vendida":0, "Precio":df["Precio"].mean()}
df_rellenados = df.fillna(valores_nuevos)
print(df_rellenados)

# Cambiar tipos de datos
# Queremos que la cantidad vendida ya no sea flotante sino entera
#                 vvvvvvvvvvvvvvvv
#    Id_producto  Cantidad_vendida     Precio
# 0         1001                30  20.500000
# 1         1002                 0  15.000000
# 2         1003                25  19.333333
# 3         1003                25  22.500000
df_rellenados["Cantidad_vendida"] = df_rellenados["Cantidad_vendida"].astype(int)
print(df_rellenados)

# Eliminar duplicados
# aqui buscará cuando todas las series contengan los mismos valores, lo cual
# en nuestro ejemplo no cumple ya que no todos los valores son iguales
df_unicos = df_rellenados.drop_duplicates()
print(df_unicos)

# Eliminamos bajo el criterio de los duplicados en la columna Id_producto
#    Id_producto  Cantidad_vendida     Precio
# 0         1001                30  20.500000
# 1         1002                 0  15.000000
# 2         1003                25  19.333333   <-- Elimino el segundo repetido
df_unicos = df_rellenados.drop_duplicates(subset='Id_producto')
print(df_unicos)

