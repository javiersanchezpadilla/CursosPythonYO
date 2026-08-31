""" Fusionar DataFrames con merge 2

    Imagina que estás trabajando con dos conjuntos de datos: uno que contiene 
    información sobre cursos en línea ofrecidos (cursos) y otro que contiene 
    información sobre las inscripciones a estos cursos (inscripciones).

    Los DataFrames se definen de la siguiente manera:

    cursos = pd.DataFrame({'curso_id': [101, 102, 103],
                           'nombre_curso': ['Introducción a Python', 
                           'Data Science con Python', 'Machine Learning Avanzado']
                          })
    
    inscripciones = pd.DataFrame({'curso_id': [102, 102, 101, 104],
                                  'fecha_inscripcion': ['2023-01-15', 
                                  '2023-02-01', '2023-01-20', '2023-03-05']})

    Tu tarea es fusionar cursos con inscripciones (en un DataFrame llamado: 
    cursos_inscripciones) de tal manera que el resultado final incluya todos 
    los registros de inscripciones, completándolos con la información 
    disponible en cursos.
    Utiliza el método de fusión adecuado para garantizar que no se pierda ninguna 
    inscripción, incluso si el curso correspondiente no está listado en el 
    DataFrame cursos. Es importante que el DataFrame resultante 
    cursos_inscripciones muestre claramente qué inscripciones no tienen un 
    curso correspondiente, rellenando esos espacios con NaN.
"""
import pandas as pd 

cursos = pd.DataFrame({'curso_id': [101, 102, 103],
                       'nombre_curso': ['Introducción a Python', 
                                        'Data Science con Python', 
                                        'Machine Learning Avanzado']})
 
inscripciones = pd.DataFrame({'curso_id': [102, 102, 101, 104],
                              'fecha_inscripcion': ['2023-01-15', '2023-02-01', 
                                                    '2023-01-20', '2023-03-05']
                             })

cursos_inscripciones = pd.merge(cursos, inscripciones, on='curso_id', how='right')
print(cursos_inscripciones)
