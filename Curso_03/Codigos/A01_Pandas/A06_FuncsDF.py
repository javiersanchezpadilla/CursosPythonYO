""" Funcionalidades de los data Frame 

    Metodos:
    --------
    df.head(n)  Muestra un numero de lineas del encabezado del data frame
                sin argumentos el valor es 5
    df.tail(n)  Muestra los últimos elementos (cola) del data frame, sin
                argumentos el valor es 5
    df.info()   Devuelve información relevante de nuestro data frame
    df.describe() DEvuelve información estadistica general del data frame
                
    Atributos:
    ----------
    shape       Muestra el número de filas y el total de columnas sin contar
                la columna del índice
    columns     Devuelve una lista con los encabezados de las columnas, que 
                realmente son los nombres de las series
    
    
    Explicación de los resultados de el método df.desribe()
    -------------------------------------------------------
    
    Métrica     Significado en palabras sencillas
    ---------------------------------------------
    count       ¿Cuántos datos válidos hay? Es el número total de valores 
                no nulos (no vacíos) presentes en esa columna.
                Si tienes 100 registros en total, pero count te da 95, 
                significa que hay 5 personas a las que se les olvidó poner su 
                edad.
    mean        ¿Cuál es el promedio general? Es el promedio aritmético de 
                todos los datos. Se calcula sumando todos los valores de la 
                columna y dividiendo la suma entre el número total de datos.
                Si la suma de todas las edades da 3,000 y hay 100 personas, 
                el mean será 30.0. En promedio, el grupo tiene 30 años.
    std         ¿Los datos están juntos o muy dispersos? Indica qué tan 
                dispersos o alejados están los datos respecto al promedio(mean)
                Una desviación baja (ej. std = 2.1) significa que casi todos 
                en el grupo tienen edades muy cercanas a los 30 años 
                (entre 28 y 32).
                Una desviación alta (ej. std = 15.4) significa que tienes un 
                grupo muy variado, con niños pequeños y personas adultas mayores.
    min         El dato más bajo de todos. El valor más pequeño registrado en 
                la columna. Si min es 18, la persona más joven del grupo tiene 
                18 años.

    Los Cuartiles (25%, 50%, 75%) y el max
    --------------------------------------
    Para entender estos tres porcentajes, imagina que ordenas a todas las 
    personas de la más joven a la más grande en una fila.
                
    25%         Primer Cuartil o Q1, es el límite del primer 25% de la muestra
                El valor debajo del cual se encuentra el 25% de los datos.
                Si el valor es 22, significa que la cuarta parte de tu grupo 
                (el 25%) tiene 22 años o menos.
    50%         Mediana o segundo cuartil Q2, es el centro exacto (Mediana)
                Es el punto medio exacto de tus datos. El 50% de las personas 
                está por debajo de este valor y el otro 50% está por encima.
                Si 50% es 28, la mitad del grupo tiene menos de 28 años y la 
                otra mitad tiene más de 28.
                A diferencia del promedio (mean), la mediana (50%) no se ve 
                afectada si metes a un multimillonario o a un anciano de 110 
                años a los datos; por eso ayuda a ver la realidad central.
    75%         Tercer cuartil Q3, es el límite del 75% de la muestra.
                El valor debajo del cual se encuentra el 75% de los datos.
                Si el valor es 40, significa que el 75% del grupo tiene 40 
                años o menos (y solo el 25% restante es más grande que 40).
    max         El dato más alto de todos. El valor más grande registrado en 
                la columna. Si max es 75, la persona más grande del grupo 
                tiene 75 años.
   
    Si tienes columnas de texto (no numéricas) y quieres ver sus estadísticas 
    (como cuántos valores únicos hay o cuál es el que más se repite), puedes 
    usar df.describe(include='all')
    
    Ejemplo práctico sobre el uso de los cuartiles
    ----------------------------------------------
    
    Imagina que hiciste un examen de programación y en la clase son 100 alumnos
    El profesor revisa todos los exámenes y ordena a todos los alumnos en una 
    fila, desde la calificación más baja hasta la más alta:
    El alumno al principio de la fila sacó 20/100 (el peor examen) (min).
    El alumno al final de la fila sacó 100/100 (el examen perfecto) (max).
    Para entender cómo le fue al grupo en general, el profesor decide dividir 
    a los 100 alumnos en 4 grupos iguales (de 25 alumnos cada uno) poniendo 
    banderitas de corte. Esas banderitas son los cuartiles.
    
    [Inicio de la fila] -------------------------------------------- [Fin de la fila]
    Calificación:      20        45           65            80           100
    Posición:        (Mínimo)   (25%)        (50%)         (75%)      (Máximo)
                                 |            |             |
                                 Q1           Q2            Q3
                            (Banderita 1) (Banderita 2) (Banderita 3)
    
    ¿Qué significan las calificaciones en cada banderita?
    -----------------------------------------------------
    Primer Cuartil (25% / Q1) = 45 puntos
    Te dice la calificación del alumno que está parado justo al terminar el 
    primer cuarto de la fila (alumno 25).
    ¿Qué significa para ti? Si sacaste menos de 45 puntos, estás en el 25% con 
    las calificaciones más bajas de la clase.

    Segundo Cuartil (50% / Mediana / Q2) = 65 puntos
    Es la calificación del alumno parado exactamente a la mitad de la fila 
    (alumno 50).
    ¿Qué significa para ti? Exactamente la mitad de la clase sacó menos de 65, 
    y la otra mitad sacó más de 65. Es tu punto de equilibrio real.

    Tercer Cuartil (75% / Q3) = 80 puntos
    Es la calificación del alumno parado casi al final (alumno 75).
    ¿Qué significa para ti? Si sacaste un 80, superaste al 75% de toda la clase
    Solo un 25% de tus compañeros sacó una nota mejor que tú.

    ¿Para qué sirven en la vida real? (El truco del 50% central)
    ------------------------------------------------------------
    Los cuartiles te dicen de un vistazo dónde se concentra la mayoría de la 
    gente.
    Entre el 25% (45 pts) y el 75% (80 pts) está el bloque del medio: el 50% 
    central de los alumnos.
    Si analizas un negocio, un conjunto de datos en Pandas, o sueldos en una 
    empresa:
    El Mínimo y Máximo te muestran los casos raros o extremos (alguien que sacó 
    0 o alguien que sacó 100).
    Los Cuartiles (25% a 75%) te muestran el comportamiento normal o la zona 
    donde cae la mitad de todos tus datos.
    
"""

import pandas as pd 
from pathlib import Path 

ruta = Path(__file__).resolve().parent 
ruta = ruta / 'ArchivosExternos/Precipitaciones.csv'

df = pd.read_csv(ruta)

# metodo head()
print("Mostrando las primetas cinco lineas del encabezado")
print(df.head())

print("\n\nMostrando las primeras tres lineas")
print(df.head(3))

# meteodo tail()
print("Mostrando los últimos cinco elementos del data frame")
print(df.tail())

print("Mostrando los últimos tres elementos")
print(df.tail(3))

# Atributo shape 
print("El data Frame es de")
print(df.shape)
renglones, columnas = df.shape
print(f"Renglones {renglones}, por {columnas} columnas")

# Atributo columns
print("Las columnas son:")
print(df.columns)

# metodo df.info()
print("\n\nInformación General de nuestro data Frame")
print(df.info())

# Información general y estadistica de nuestro data Frame
print("\n\n")
print(df.describe())



