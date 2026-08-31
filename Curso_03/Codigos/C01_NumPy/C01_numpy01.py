import pandas as pd 
import numpy as np 
from pathlib import Path 

ruta = Path(__file__).resolve().parent
ruta = ruta / 'ArchivosExternos/Ciudades_Visitadas_Latinoamerica_2023.csv'
print(ruta)

df = pd.read_csv(ruta)
print(df.head())

