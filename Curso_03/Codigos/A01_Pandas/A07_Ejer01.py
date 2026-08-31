""" Ejercicio DataFrames en Pandas 1

    Crea un DataFrame llamado datos_clima usando Pandas para cargar un archivo 
    CSV llamado clima.csv que supuestamente contiene datos sobre temperaturas 
    y precipitaciones en diferentes ciudades. Asegúrate de importar Pandas 
    antes de intentar cargar el archivo.
    Considera que tu archivo clima.csv se encuentra dentro de una carpeta 
    llamada ArchivosExternos
    Muestra un resumen estadistico del data frame,
    Asigna a variables la primer linea y la última linea del data frame
    muestra los resultados
"""
import pandas as pd 
from pathlib import Path 

ruta = Path(__file__).resolve().parent
ruta = ruta / 'ArchivosExternos/clima.csv'
df = pd.read_csv(ruta)
print("Resumen Estadistico")
print(df.describe())

inicio = df.head(1)
final = df.tail(1)

print("\nPrimer linea del data frame")
print(inicio)

print("\n Final del data frame")
print(final)
