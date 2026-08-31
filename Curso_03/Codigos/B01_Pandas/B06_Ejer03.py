""" Fusionar DataFrames con merge 3

    Dispones de dos DataFrames, productos y reviews, que contienen información 
    sobre productos y las reseñas asociadas a estos productos, respectivamente. 
    Los DataFrames se presentan de la siguiente manera:

    productos = pd.DataFrame({'ID': [10, 11, 12],
                                'Nombre': ['Teclado', 'Mouse', 'Monitor'],
                                'Marca': ['Logitech', 'Razer', 'Dell']})
    
    reviews = pd.DataFrame({'ID': [10, 11, 12],
                            'Calificación': [5, 4, 4],
                            'Comentario': ['Excelente producto', 
                                            'Buen producto', 'Satisfecho']})

    Tu tarea consiste en fusionar productos con reviews para obtener un 
    DataFrame que combine la información de ambos (al cual debes nombrar: 
    productos_reviews), manteniendo los índices originales de cada uno.
    Utiliza los parámetros adecuados de la función merge() para realizar esta 
    combinación. El DataFrame resultante productos_reviews debe contener las 
    columnas de ambos DataFrames originales, permitiendo así un análisis 
    detallado de cada producto junto con sus reseñas.
"""
import pandas as pd 

productos = pd.DataFrame({'ID': [10, 11, 12],
                            'Nombre': ['Teclado', 'Mouse', 'Monitor'],
                            'Marca': ['Logitech', 'Razer', 'Dell']})

reviews = pd.DataFrame({'ID': [10, 11, 12],
                        'Calificación': [5, 4, 4],
                        'Comentario': ['Excelente producto', 
                                            'Buen producto', 'Satisfecho']})

productos_reviews = pd.merge(productos, reviews, left_index=True, right_index=True)
print(productos_reviews)

""" 
    No podemos usar on='ID' porque los parámetros on y left_index, right_index
    representan dos formas completamente opuestas e incompatibles de unir datos 
    en Pandas

    Si usamos on='ID' nos da un error
    El parámetro on='ID' le dice a Pandas: Busca la columna llamada 'ID' dentro 
    de las tablas y une las filas donde los números de esa columna coincidan
    Los parámetros left_index=True, right_index=True le dicen a Pandas: 
    Ignora completamente los nombres y valores de las columnas. Une la fila 0 
    con la fila 0, la fila 1 con la fila 1, etc., guiándote por el número de 
    posición (índice) de la tabla,para probar podemos cambiar los valores de ID
    en cualquiera de los data frame y el resultado será el mismo ya que no toma
    el ID como base para unir la tablas.
    Sin embargo Usar on='ID' es mucho más seguro que usar índices. Si el día 
    de mañana los productos en reviews vienen desordenados (por ejemplo, el 
    ID: 12 al principio), on='ID' seguirá uniendo cada reseña con su producto 
    correcto, mientras que unir por índice (left_index=True) mezclaría 
    información de productos distintos.
"""