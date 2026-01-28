""" Filtrar palabras """

frase = "Acapulco, guerrero, enero de 2025"

print(f'Cuantas veces se repite la letra "a" {frase.lower().count('a')}')

# contar el número de palabras
frase2 = "   Acapulco guerrero enero de 2025    "
# debemos quitar los espacios al inicio y al final y el nume de espacios +1 = palabras
print(f'El total de palabras es {(frase2.strip().count(" ")) + 1}')

# crear una lsita de estos elementos
print(frase2.strip().split())
frase.split
