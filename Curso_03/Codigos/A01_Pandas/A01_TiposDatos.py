""" Los tipos de datos basicos en pandas son
    Series (las columnas de una hoja)
    DataFrame (Toda la hoja con columnas y renglones)
"""

datos = {"nombre": ["Pedro", "Juan", "Lorena"], "edad":[25, 33, 56]}
print(datos)
print(type(datos))

# Importando pandas
import pandas as pd 

# Creamos un valor del tipo DataFrame
df = pd.DataFrame(datos)
print(df)

# Accediendo a una serie, lo podemos hacer de dos maneras: 
# 1) por el nombre del índice
print(df["nombre"])

# 2) por la refencia de la variable del tipo DataFrame
print(df.nombre)

print("El dataFrame es del tipo:", type(df))
print("La columna nombre es del tipo:", type(df["nombre"]))
print("La columna edad es del tipo:", type(df.edad))

""" Las Series tienen una sola dimensión y 2 atributos índice y valor
    Los DataFrame tienen dos dimensiones (largo y ancho), además tienen 
    tres atributos índice, columnas y renglones
"""