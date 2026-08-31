""" MAS DE LOS DATA FRAME

    Operaciones con los data frame
"""

import pandas as pd 

datos = {'Nombre': ['Ana', 'Luis', 'Carlos', 'Sara'],
        'Edad':[25, 30, 22, 27],
        'Ciudad': ['Acapulco', 'Iguala', 'Chilpancingo', 'Morelos']}

df = pd.DataFrame(datos)
print(df)

# Agregar una columna al data frame (es igual a los diccionarios)
df['Salario'] = [10000, 15000, 20000, 8000]
print(df)

# Modificar el contenido de una serie del data frame (columna)
df['Salario'] = df['Salario'] + 2000
print(df)

# Crear una serie a partir del data frame
nombres = df['Nombre']
print(nombres)

# filtrado de valores. Crear un data frame de aquellos mayores a 25
mayores_25 = df[df['Edad'] > 25]
print(mayores_25)

# Tambien podemos crear una variable para el criterio
criterio = df['Edad'] > 25
mayores_25_ver_2 = df[criterio]
print(mayores_25_ver_2)
