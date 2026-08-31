""" Fusionar DataFrames con merge 1

    Tienes dos DataFrames, libros y autores, que necesitas fusionar.
    Estos DataFrames se definen de la siguiente manera:

    libros = pd.DataFrame({
        'ID': [1, 2, 3, 4],
        'titulo': ['El Quijote', 'La Odisea', 'Cien Años de Soledad', 
        'El Principito']
    })
    
    autores = pd.DataFrame({
        'ID': [1, 2, 3, 5],
        'nombre': ['Miguel de Cervantes', 'Homero', 'Gabriel García Márquez', 
        'J.K. Rowling']
    })
    
    El objetivo es fusionar libros con autores para obtener un DataFrame que 
    contenga toda la información disponible, asociando cada libro con su autor 
    correspondiente. Debes nombrar el DataFrame fusionado como: libros_autores
    Utiliza el método de fusión adecuado para asegurar que no se pierda ningún 
    libro o autor, incluso si no hay una correspondencia directa entre ellos. 
    El resultado debe tener NaN donde no haya información disponible.
"""
import pandas as pd 

libros = pd.DataFrame({ 'ID': [1, 2, 3, 4],
                        'titulo': ['El Quijote', 'La Odisea', 
                                   'Cien Años de Soledad', 'El Principito']})

autores = pd.DataFrame({ 'ID': [1, 2, 3, 5],
                         'nombre': ['Miguel de Cervantes', 'Homero', 
                                    'Gabriel García Márquez', 'J.K. Rowling']})

libros_autores = pd.merge(libros, autores, on='ID', how='outer')
print(libros_autores)
