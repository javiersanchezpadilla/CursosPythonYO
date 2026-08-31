numeros = range(10)
print(type(numeros))    # objeto del tipo range
print(numeros)          # Salida: range(0, 10)

for numero in numeros:
    print(numero)

print('---------5--------------')
for a in range(5):
    print(a)

print('------5, 10-----------------')
for a in range(5, 10):
    print(a)

print('----------Hola a todos-------------')
palabra='Hola a todos'
for a in range(len(palabra)):
    print(a)

print('----------10, 0, -2-------------')
for i in range(10, 0, -2):
    print(i)
    
print('-----Pares del 2 al 20------------')
for i in range(2, 21, 2):
    print(i)
    