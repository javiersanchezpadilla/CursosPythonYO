""" Operaciones con series


"""

import pandas as pd 

serie = pd.Series([10, 20, 30, 40, 50])
print(serie)

# Afectamos un valor en la serie
serie[0] +=100
print(serie)

# Afectamos toda la serie
serie *= 100
print(serie)


