# Manejo de tuplas

a = 1, 2, 3
print(type(a))
print(a)

b = ("casa", "libro", "gato", "perro", "perico", "silla")
print(type(b))
print(b)

sub_tupla = b[2:4]
print(sub_tupla)

# b[1] = "canario" las tuplas son inmutables

print('desempaquetando las tuplas')
(v1, v2, v3, v4, v5, v6) = b
print(v1)
print(v2)
print(v3)
print(v4)
print(v5)
print(v6)

# print(dir(b))
# print(help(b.indexq))

f = ( 1, 1, 1, 2, 2, 4, 5, 4, 3, 4, 5, 6, 1)
print(f.count(1))
print(f.index(2))
print(b.index("perico"))

auto = ('Ford', 'Fiesta', 'Rojo', 2022, 5)
(marca, modelo, color, modelo, puertas) = auto
print(marca)
print(color)
print(modelo)
print(puertas)
print (marca, modelo)

print(f)
temporal = list(f)
temporal.append(100)
f = tuple(temporal)
print(f)