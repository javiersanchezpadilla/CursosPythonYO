a = 10
b = 20
print(f'El valor de "a" es {a}')
print(f'El valor de "b" es {b}')

a, b = b, a
print(f'El valor de "a" es {a}')
print(f'El valor de "b" es {b}')

numeros = [1, 2, 3, 4, 5, 6]
primero, *resto = numeros

print(numeros)
print(primero)  # Imprime 1
print(resto)  # Imprime [2, 3, 4, 5, 6]