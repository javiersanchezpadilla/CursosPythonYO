""" Uso de Merge()"""

import pandas as pd 

df1 = pd.DataFrame({'ID':[1, 2, 3],
                    'Nombre':['Ana', 'Luis', 'Carlos']})

df2 = pd.DataFrame({'ID':[1, 2, 4],
                    'Edad':[25, 30, 22]})

print(df1)
print(df2)

# Por defecto tiene implicito how=inner
print("\nCON VALOR HOW IMPLICITO POR DEFECTO")
df_combinado = pd.merge(df1, df2, on='ID')
print(df_combinado)

# HOW = inner
print("\nCON VALOR HOW = inner")
df_combinado = pd.merge(df1, df2, on='ID', how='inner')
print(df_combinado)

# HOW = outer
print("\nCON VALOR HOW = outer")
df_combinado = pd.merge(df1, df2, on='ID', how='outer')
print(df_combinado)

# HOW = left (todos los del dataframe izquierdo)
print("\nCON VALOR HOW = left")
df_combinado = pd.merge(df1, df2, on='ID', how='left')
print(df_combinado)

# HOW = right
print("\nCON VALOR HOW = right")
df_combinado = pd.merge(df1, df2, on='ID', how='right')
print(df_combinado)

# Para mantener la referencia del índice de origen de cada dataframe
# agrega dos columnas mas, donde indica el índice de origen de cada dataframe
print("\nMantener la referencia de los indices de origen")
df_indexado = pd.merge(df1, df2, left_index=True, right_index=True)
print(df_indexado)
