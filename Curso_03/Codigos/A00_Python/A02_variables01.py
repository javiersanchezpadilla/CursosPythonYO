""" USO DE VARIABLES

    En Python, las variables son contenedores que utilizamos para almacenar 
    datos en la memoria de la computadora mientras se ejecuta un programa. A 
    diferencia de otros lenguajes de programación más rígidos, declarar y usar 
    variables en Python es extremadamente sencillo y flexible.

    1. Creación y Asignación de Variables
    -------------------------------------
    En Python, no necesitas declarar el tipo de datos de una variable de forma 
    explícita antes de usarla, ni se utiliza alguna palabra clave especial 
    (como var, let o int). La variable se crea en el instante en que le 
    asignas un valor mediante el operador de igualdad (=):
    
    2. Tipado Dinámico y Fuertemente Tipado
    ---------------------------------------
    Python destaca por dos características clave en la gestión de sus variables:
    Tipado Dinámico: El tipo de dato asociado a la variable se deduce 
    automáticamente según el valor que le asignes. Además, una misma variable 
    puede cambiar de tipo durante la ejecución del programa:
    
    3. Reglas y Convenciones de Nombres (PEP 8)
    -------------------------------------------
    Para que tus programas funcionen sin errores y tu código sea fácil de leer, 
    debes seguir las reglas del lenguaje y las mejores prácticas recomendadas 
    por la guía de estilo PEP 8:

    Reglas obligatorias (si no las sigues, el código falla):
    1.  Sensible a mayúsculas y minúsculas: Edad, edad y EDAD son tres variables 
        distintas.
    2.  Caracteres permitidos: Solo pueden contener letras (a-z, A-Z), números 
        (0-9) y guiones bajos (_).
    3.  Inicio de nombre: Un nombre de variable nunca puede comenzar con un 
        número (ej. 1usuario es inválido).
    4.  Palabras reservadas: No puedes usar palabras clave del lenguaje 
        (como if, for, def, class, import, etc.).

    Convenciones recomendadas por PEP 8:
    ------------------------------------
    Utilizar el estilo snake_case: Todo en minúsculas y las palabras separadas 
    por guiones bajos.
    Usar nombres descriptivos que expliquen el contenido o propósito del dato.
    n = 'JAvier' (muy ambiguo)  nombre_usuario = 'JAvier' (ok)
    
    4. Asignación Múltiple y Reorganización de Valores
    --------------------------------------------------
    Python permite realizar asignaciones avanzadas de forma concisa y elegante 
    en una sola línea de código.
    
    Asignar un mismo valor a varias variables:
    ------------------------------------------
    Se puede asignar de manera simultanea (a = b = c = d = 10)
    
    Intercambiar valores entre variables (Swap):
    --------------------------------------------
    En la mayoría de los lenguajes necesitas una variable temporal, pero en 
    Python se hace de forma directa:
    
    6. Las Variables en Python son Referencias a Objetos
    ----------------------------------------------------
    En un nivel un poco más avanzado, es útil saber que en Python todo es un 
    objeto. Cuando creas una variable, realmente no estamos guardando un valor 
    dentro de una caja, sino que estás creando una etiqueta (o apuntador) que 
    hace referencia a un objeto en la memoria RAM.
"""
# Sintaxis básica: nombre_variable = valor

# 1. Creación y Asignación de Variables
nombre = "Rodrigo"     # Almacena una cadena de texto (str)
edad = 25              # Almacena un número entero (int)
estatura = 1.75        # Almacena un número decimal (float)
es_estudiante = True   # Almacena un valor booleano (bool)

# 2. Tipado Dinámico y Fuertemente Tipado
x = 10       # 'x' es un número entero
x = "Diez"   # Ahora 'x' pasa a ser un texto sin marcar un error

# 4. Asignación Múltiple y Reorganización de Valores
x, y, z = 1, 2, 3
print(x)
print(y)
print(z)

# Asgignación simultanea de valores a las variables
a = b = c = d = e = 20
print(a)
print(b)
print(c)
print(d)
print(e)

# Intercambiar valores entre variables (Swap):
a = 10
b = 20
print(a)
print(b)
a, b = b, a 
print(a)
print(b)

# 6. Las Variables en Python son Referencias a Objetos
a = [1, 2, 3]
b = a  # 'b' no duplica la lista, apunta a la MISMA lista en memoria

b.append(4)
print(a) # Imprime [1, 2, 3, 4] porque ambas variables apuntan al mismo objeto
