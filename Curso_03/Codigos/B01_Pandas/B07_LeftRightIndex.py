""" USAR SOLO UN ARGUMENO LEFT_INDEX O RIGHT_INDEX

    Como usar al definir una instrucción uno solo de los argumentos, usar solo 
    left_index=True o solo right_index=True en lugar de usar ambos como se ha 
    visto, si fuera el caso ¿como funcionaria?
   
    por ejemp
    En lugar de usar la instrucción así:
    
    productos_reviews = pd.merge(productos, reviews, left_index=True, right_index=True)
    
    Usarla así:
    productos_reviews = pd.merge(productos, reviews, left_index=True)   <-- left
    productos_reviews = pd.merge(productos, reviews, right_index=True)  <-- right
    
    Lo anterior es totalmente válido usar solo uno de los dos, pero tiene una 
    regla muy importante: se tiene que combinar obligatoriamente con el otro 
    lado correspondiente usando left_on o right_on.
    Es decir, no puedes poner solo left_index=True y dejar el lado derecho 
    'en el aire'; tienes que decirle a Pandas contra qué columna del lado 
    derecho quieres comparar ese índice.

    ¿Cómo funciona en la práctica?
    ------------------------------
    Imagina que tienes una tabla donde la información clave está en el índice 
    y otra tabla donde esa misma información está guardada en una columna normal.

    Las dos combinaciones válidas son:
    left_index=True + right_on='nombre_columna': Usa el índice de la tabla 
                                                 izquierda y lo busca dentro 
                                                 de una columna de la tabla 
                                                 derecha.

    left_on='nombre_columna' + right_index=True: Busca los valores de una 
                                                 columna de la tabla izquierda 
                                                 dentro del índice de la tabla 
                                                 derecha.
                                                 
    No es posible omitirlo o de lo contrario Pandas arrojara un error, ya que
    exige que le aclares cómo debe cruzar la información con la otra tabla 
    (izquierda o derecha).                                   
"""
import pandas as pd

# Tabla 1: Los ID están en el ÍNDICE (0, 1, 2 son reemplazados por 10, 11, 12)
productos = pd.DataFrame(
    {'Nombre': ['Teclado', 'Mouse', 'Monitor'],
     'Marca': ['Logitech', 'Razer', 'Dell']},
    index=[10, 11, 12]  # <-- El ID es el índice
)

# Tabla 2: El ID es una COLUMNA normal
reviews = pd.DataFrame(
    {'ID_Producto': [10, 11, 12], # <-- El ID es una columna
     'Calificación': [5, 4, 4],
     'Comentario': ['Excelente producto', 'Buen producto', 'Satisfecho']}
)

# Usamos el ÍNDICE de la izquierda (productos) y la COLUMNA de la derecha 
# (reviews)
productos_reviews = pd.merge(
    productos, 
    reviews, 
    left_index=True,          # Usar el índice de 'productos'
    right_on='ID_Producto'    # Buscarlo en la columna 'ID_Producto' de 'reviews'
)

print(productos_reviews)