""" DESEMPAQUETADO DE VALORES  """

numeros = [1, 2, 3, 4, 5, 6]
primero, *resto = numeros

print(numeros)
print(primero)      # Imprime 1
print(resto)        # Imprime [2, 3, 4, 5, 6]

print("\nExtracción de valores")
uno, *medio, ultimo = numeros
print(numeros)
print(uno)          # Imprime 1
print(medio)        # imprime [2, 3, 4, 5]
print(ultimo)       # Imprime 6
