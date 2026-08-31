""" Agregación de series en Pandas

    En Pandas, las funciones de agregación son aquellas que toman una serie de 
    datos (una columna) y la reducen a un solo valor representativo.
    Son fundamentales cuando necesitas resumir información, calcular métricas 
    rápidas
"""
import pandas as pd 

numeros = pd.Series([10, 20, 30, 40, 50, 10, 10])
print(numeros)

# ESTADISTICAS ESCRIPTIVAS Y CENTRALES
# ------------------------------------

# Suma de todos los valores de la serie
print('La suma de los valores', numeros.sum())

# Calculamos el promedio artimetico
print('Valor promedio', numeros.mean())

# Calcula la mediana (el valor que está justo a la mitad)
print('La mediana es', numeros.median())

# Devuelve el valor que mas se repite (la moda). 
# (Nota: devuelve una Serie con las modas en caso de que haya empates).
print('La moda es', numeros.mode())

# VALORES EXTREMOS Y CONTEOS
# --------------------------

numeros2 = pd.Series([10, 20, 30, 40, 50, None, 10, 10, 20, None, 100])

# Valor máximo
print('El valor máximo', numeros2.max())

# Valor mínimo
print('El valor minímo', numeros2.min())

# Cuenta la cantidad de elementos no nulos (ignora los NaN)
print('Elementos no NaN', numeros2.count())

# Cuenta cuántos valores únicos o distintos existen en la serie
# ignora los NaN, los únicos son [10, 20, 30, 40, 50, 100]
print('Elementos unicos', numeros2.nunique())

# MEDIDAS DE DISPERSIÓN Y VARIACIÓN
# ----------------------------------
edades = pd.Series([18, 22, 25, 30, 45, 60])

# Calcula la desviación estándar (qué tan dispersos están los datos del promedio)
print(edades.std())           # 15.82

# Devuelve el cuantil o percentil solicitado en el rango de 0 a 1.
# Por ejemplo, .quantile(0.5) es equivalente a la mediana, y 
# .quantile(0.75) al tercer cuartil
print(edades.quantile(0.75))  # 41.25 (tercer cuartil / 75%)

# EL PODER DE AGG() AGGREGATE()
# ----------------------------

# Aplicamos múltiples agregaciones en un solo paso
resumen1 = edades.agg(['min', 'max', 'mean', 'std'])
print(resumen1)

# Nos da el mismo resultado que la versión anterior
resumen2 = edades.aggregate(['min', 'max', 'mean', 'std'])
print(resumen2)
