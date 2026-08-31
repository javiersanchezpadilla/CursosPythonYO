""" Lectura de archivos externos CSV 

    Esta es la forma de leer un archivo CSV, sin embargo la ruta se tiene
    que manejar como una cadena de texto lo cual no es eficiente
"""

import pandas as pd 

# OPCION 1. de lectura del archivo, indicando toda la cadena de la ruta
# df = pd.read_csv('/home/javier/Documentos/Programas/Python/InterSem/A01_Pandas/ArchivosExternos/Precipitaciones.csv')

# OPCION 2. indicando la ruta a traves de una cadena de texto 
# ruta = '/home/javier/Documentos/Programas/Python/InterSem/A01_Pandas/ArchivosExternos/Precipitaciones.csv'

# OPCION 3. Si se desea se puede cortar la cadena en dos partes usando la contrabarra
            # ruta = '/home/javier/Documentos/Programas/Python/InterSem/A01_Pandas/'\
            #        'ArchivosExternos/Precipitaciones.csv'

            # df = pd.read_csv(ruta)

# print(df)

# El manejo de la ruta como una cadena de texto no es lo mas eficiente, se 
# recomienda el manejo de la ruta como un objeto
import pandas as pd 

ruta = "/home/javier/Documentos/Programas/Python/InterSem/A01_Pandas/ArchivosExternos/Precipitaciones.csv"

df = pd.read_csv(ruta)

print(df.head(2))
print(df.tail(2))

