numeros = range(10)
print(type(numeros))    # objeto del tipo range
print(numeros)          # Salida: range(0, 10)

for numero in numeros:
    print(numero)

print('-----------------------')
for a in range(5):
    print(a)

print('-----------------------')
for a in range(5, 10):
    print(a)

print('-----------------------')

palabra='Hola a todos'
for a in range(len(palabra)):
    print(a)

for i in range(10, 0, -2):
    print(i)