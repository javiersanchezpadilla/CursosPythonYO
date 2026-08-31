""" Trabajar con DataFrames de Pandas 3

    Partiendo del DataFrame df mencionado anteriormente:

        data = { 'Nombre': ['Ana', 'Luis', 'Carlos', 'Sara'],
                'Edad': [25, 30, 22, 27],
                'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Bilbao']
                }

    Realiza las siguientes operaciones:
    -----------------------------------
    Crea un dataframe llamado df
    Agrega una nueva columna llamada Edad_en_10_años que contenga la edad de 
    las personas dentro de 10 años.
    Modifica la columna Ciudad para que todas las ciudades estén en mayúsculas
    Crea una nueva columna Es_Mayor_de_25 que contenga valores booleanos: True 
    si la persona tiene 25 años o más, y False en caso contrario.
"""
import pandas as pd 

data = { 'Nombre': ['Ana', 'Luis', 'Carlos', 'Sara'],
         'Edad': [25, 30, 22, 27],
         'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Bilbao']}

df = pd.DataFrame(data)
df['Edad_en_10_años'] = df['Edad'] + 10
# usamos un descriptor
df['Ciudad'] = df['Ciudad'].str.upper()
df['Es_mayor_de_25'] = df['Edad'] > 25
print(df)
