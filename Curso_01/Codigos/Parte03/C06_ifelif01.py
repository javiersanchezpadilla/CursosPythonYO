edad =  15  # int(input('Dime tu edad'))

if edad >= 18:
    print('Adulto')
else:
    print('Menor')

if edad >= 18:
    print('Adulto')
elif edad >= 13:
    print('Adolescente')
else:
    print('Menor')

x1, x2, x3 = int(input('ingresa x1: ')), int(input('ingresa x2: ')), int(input('ingresa x3: '))
print(f'x1={x1}, x2={x2}, x3={x3}')

if x1 > x2:
    if x1 > x3:
        maximo = x1
    else:
        maximo = x3
elif x2 > x3:
    maximo = x2
else:
    maximo = x3


print(f'El mayor de los tres valores es {maximo}')
