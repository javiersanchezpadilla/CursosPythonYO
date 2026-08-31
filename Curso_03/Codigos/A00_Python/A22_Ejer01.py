"""
Escribe un programa que use la función range() para sumar todos los números del 1 al 100.
Para ello sigue los siguientes pasos:
Inicializa la variable suma = 0.
Usa un bucle for para iterar sobre cada número del 1 al 100, incluyendo el 100.
Imprime el resultado de la suma empleando el siguiente mensaje:
"La suma de todos los números del 1 al 100 es: {suma}"
Pista:
En cada paso del bucle, actualiza la variable suma incrementándola con el valor del número 
actual en la iteración. De esta manera, suma acumulará el total de todos los números procesados 
hasta ese momento.
"""
suma = 0
for numero in range(1, 101):
    suma = suma + numero
print (f"La suma de todos los números del 1 al 100 es: {suma}")
