mi_lista = []
print(type(mi_lista))

frutas = ["manzana", "pera", "melon", "sandia"]
print(type(frutas))
print(frutas)

print(frutas[0])    # Acceder a los miembros de una lista
print(frutas[1])
print(frutas[2])

print(frutas)       # Como cambiar los elementos de una lista
frutas[2] = 'piña'
print(frutas)

print(frutas)       # Agregar una fruta al final de la lista
frutas.append('uvas')
print(frutas)

print(frutas)       # Agregar una fruta en un indice
frutas.insert(0,'naranja')
print(frutas)

print(frutas)       # Eliminar una fruta en un indice
frutas.remove('piña')
print(frutas)

mis_listas = [[1, 2, 3, 4], ['a', 'b'], ['Pablo', 'Jorge', 'Sara'], [1.2, 3.1416, 8.99]]
print(type(mis_listas))
print(mis_listas)

print(mis_listas)               # Muestra toda la lista
print(mis_listas[2])            # Muetra una elemento de la lista
print(mis_listas[2][2])         # Muestra un elemento dentro de la sublista
mis_listas[2].append('Wendy')   # agrega al FINAL DE UNA SUBLISTA
print(mis_listas)

print(mis_listas)
mis_listas[2][0] = 'Joaquin'    # cambiar Pablo por Joaquin
print(mis_listas)
mis_listas[2]
mis_listas[2][2]

print(frutas)
print(frutas[1:3])
print(frutas[::2])
print(frutas[::-1])

frutas.sort()               # Ordena la lista
print(frutas)

lista_numeros = [ 3, 4, 7, 1,  12, 9, -1]
print(lista_numeros)
lista_numeros.sort()
print(lista_numeros)

lista_numeros.sort(reverse=True)
print(lista_numeros)

nueva_lista = frutas + mis_listas + lista_numeros
print(type(nueva_lista))
print(nueva_lista)

lista_combinada = [[1, 2, 3], ("a", "b", "c"), [[1, 2], (100, 200, 300, 200)] ]
print(lista_combinada)
