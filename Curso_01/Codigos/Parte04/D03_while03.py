"""
Utilizando un bucle while, escribe un programa que cuente desde 0 hasta 15, 
pero que omita los números 5 y 10. Usa la declaración continue para lograr este 
comportamiento, e imprime cada número en una línea nueva.
"""
contador = 0
while contador < 15:
    contador += 1
    if contador == 5 or contador == 10:
        continue
    print(contador)
    