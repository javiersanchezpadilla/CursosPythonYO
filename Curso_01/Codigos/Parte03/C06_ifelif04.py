"""
Declara tres variables x1, x2, x3, que contengan tres números enteros distintos. 
El programa debe imprimir los números en orden ascendente.
El propósito de este ejercicio es fortalecer tu comprensión y habilidad para aplicar 
estructuras condicionales en Python, diseñando una solución que te permita practicar 
cómo controlar el flujo de un programa basado en condiciones específicas.
Es importante mencionar que, aunque existen métodos más eficientes y directos para 
ordenar números en Python —tales como las funciones sorted() o el uso de listas—, el 
enfoque de este ejercicio es que desarrolles y apliques la lógica detrás de las estructuras 
condicionales. Este enfoque te ayudará a mejorar tu pensamiento lógico y tu capacidad para 
resolver problemas de programación de una manera más fundamental.
"""

# Inicialización de variables con números enteros.
x1 = 1
x2 = 3
x3 = 2
 
# Comenzamos a determinar el orden ascendente de los números.
# Primero, verificamos si x1 es el menor de los tres.
if x1 <= x2 and x1 <= x3:
    # Dentro de este bloque, x1 es el menor.
    # Ahora, comparamos x2 y x3 para decidir el orden de los números restantes.
    if x2 <= x3:
        # Si x2 es menor o igual a x3, el orden es x1, x2, x3.
        print(x1, x2, x3)
    else:
        # Si x3 es menor que x2, el orden es x1, x3, x2.
        print(x1, x3, x2)
# En caso de que x1 no sea el menor, verificamos si x2 es el menor.
elif x2 <= x1 and x2 <= x3:
    # Dentro de este bloque, x2 es el menor.
    # Comparamos x1 y x3 para decidir el orden de los números restantes.
    if x1 <= x3:
        # Si x1 es menor o igual a x3, el orden es x2, x1, x3.
        print(x2, x1, x3)
    else:
        # Si x3 es menor que x1, el orden es x2, x3, x1.
        print(x2, x3, x1)
# Si ni x1 ni x2 son los menores, entonces x3 debe ser el menor.
else:
    # Dentro de este bloque, x3 es el menor.
    # Comparamos x1 y x2 para decidir el orden de los números restantes.
    if x1 <= x2:
        # Si x1 es menor o igual a x2, el orden es x3, x1, x2.
        print(x3, x1, x2)
    else:
        # Si x2 es menor que x1, el orden es x3, x2, x1.
        print(x3, x2, x1)
