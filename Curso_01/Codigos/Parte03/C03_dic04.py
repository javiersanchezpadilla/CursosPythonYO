"""
Con el siguiente diccionario productos que contiene productos como 
claves y sus precios como valores: 
productos = {"manzana": 0.40, "banana": 0.50, "cereza": 0.80}
Realiza las siguientes operaciones usando métodos apropiados de diccionarios: 
Guarda todas las claves del diccionario en una variable, e imprímela.
Guarda todos los valores del diccionario en una variable, e imprímela.
Añade un nuevo producto llamado "naranja" con un precio de 0.60. Imprime el resultado
Actualiza el precio de la "banana" a 0.75. Imprime el resultado
Imprime todos los pares clave-valor del diccionario actualizado.
"""
productos = {"manzana": 0.40, "banana": 0.50, "cereza": 0.80}
claves = productos.keys()
print(claves)
valores = productos.values()
print(valores)
productos["naranja"] = 0.60
print(productos)
productos["banana"] = 0.75
print(productos)
print(productos.keys(), productos.values())


