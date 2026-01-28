                    # esta secuencia
for un_numero in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(un_numero)

for una_letra in 'Esta es una cedena de texto':
    print(una_letra)

paises = ['Mexico', 'Colombia', 'Venezuela', 'Argentina', 'Peru']


una_cadenota = ''
for dato in paises:
    letras_pais = len(dato)
    una_cadenota = una_cadenota + dato
    print(f'el país {dato} tiene {letras_pais} letras')
print(una_cadenota)

for p in paises:
    if len(p) > 6:
        print(f'{p} tiene nombre largo')
    else:
        print(f'{p} tiene nombre corto')

# ciclos anidados
prendas = ['zapato', 'sombrero', 'pantalon', 'bermuda', 'camiseta']
colores = ['blanco', 'azul', 'verde']

for prenda in prendas:
    for color in colores:
        print(prenda, color)



# mi_cadena = "Acapulco, Guerrero Enero del 2025"
# mi_lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# mi_tupla = ( 10, 20, 30, 40, 50, 60, 60, 60, 70, 70, 80, 90)
# mi_dicc = {'nombre':'juan', 'edad':25, 'telefono':'7441234567'}
# mi_dicc.pop('edad')
# print(mi_dicc)

# for letra in mi_cadena:
#     print (letra)

# for elemento in mi_lista:
#     print(elemento)

# for valor in mi_tupla:
#     print(valor)

# for alumno in mi_dicc.values():
#     print(alumno)

