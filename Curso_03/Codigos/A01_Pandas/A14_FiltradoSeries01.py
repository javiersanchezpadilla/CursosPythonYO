""" Filtrado de series 

    Es aplicar criterios sobre las series de los datos
"""

import pandas as pd 

serie = pd.Series([5, 10, 15, 20, 25])

print(serie)

# CReamos un filtro
# dtype: int64
# 0    False
# 1    False
# 2    False
# 3     True    <-- Cumple el criterio
# 4     True    <-- Cumple el criterio
filtro = serie > 15
print(filtro)

# 3    20
# 4    25
print("\nAplicamos el filtro a la serie")
serie_filtrada = serie[filtro]
print(serie_filtrada)
