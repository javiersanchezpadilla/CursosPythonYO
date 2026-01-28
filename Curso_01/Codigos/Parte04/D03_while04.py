"""
Escribe un programa en Python que utilice un bucle while para imprimir números 
empezando desde 1. Utiliza la declaración break para terminar el bucle si se 
encuentra un número múltiplo de 4 (luego de haberlo impreso).
Pista:
Para determinar si un número es múltiplo de 4 puedes hacerlo de la siguiente forma:
if x % 4 == 0:
Donde x representa el número actual en la secuencia. Si x es múltiplo de 4, esta 
condición se evaluará como verdadera, y podrás utilizarla para decidir cuándo ejecutar 
la declaración break para salir del bucle.
"""
contador = 1

while contador < 100:
    print(contador)
    if contador % 4 == 0:
        break
    contador += 1
