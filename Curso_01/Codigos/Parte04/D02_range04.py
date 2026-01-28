"""
Dada la cadena de texto "aprendizaje", escribe un programa que utilice la función 
range() junto con la función len() para iterar sobre cada carácter de la cadena. 
En cada iteración, imprime el índice del carácter seguido del carácter mismo en el 
formato "Índice [n]: Carácter", donde [n] es el índice actual y Carácter es el carácter en ese índice.
Por ejemplo, la primera línea impresa debería ser "Índice 0: a".
Pista
Para ello podrás armar una cadena literal del tipo: "Índice {i}: {cadena[i]}"
Donde i es la variable que se incrementa en cada iteración del bucle for y representa el índice del 
carácter, y cadena[i] es el carácter correspondiente a ese índice en la cadena "aprendizaje"
"""
cadena = "aprendizaje"
for i in range(len(cadena)):
    print(f"Índice {i}: {cadena[i]}")