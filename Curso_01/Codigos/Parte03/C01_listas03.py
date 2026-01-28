"""
Inicialización de la lista: Se crea una lista llamada numeros con cinco 
elementos: 1, 2, 3, 4, y 5. Luego, esta lista se imprime en la consola, 
mostrando su estado inicial.
Añadir un elemento al final: Se utiliza el método adecuado para añadir el 
número 6 al final de la lista numeros. La lista modificada se imprime, 
reflejando la adición del nuevo elemento.
Eliminar el primer elemento: Se aplica el método adecuado para eliminar el 
primer elemento de la lista. Después de esta operación, la lista se imprime 
de nuevo, mostrando su estado con el primer elemento eliminado.
Insertar un elemento en una posición específica: Se usa el método adecuado 
para insertar el número 7 en la posición con índice 1 de la lista. A 
continuación, se imprime la lista, lo cual permite visualizar el cambio 
producido por la inserción.
Ordenar la lista: Finalmente, se llama al método adecuado para ordenar los 
elementos de la lista en orden ascendente. La lista ordenada se imprime, mostrando 
el resultado final de todas las operaciones realizadas.
Cada paso demuestra cómo manipular y modificar una lista en Python, incluyendo la 
adición y eliminación de elementos, así como el ordenamiento de sus contenidos. 
Este ejercicio es útil para entender cómo funcionan las listas en Python y cómo se 
pueden utilizar para almacenar y manipular colecciones de datos.
"""

numeros = [1, 2, 3, 4, 5]
print(numeros)

numeros.append(6)
print(numeros)

numeros.remove(numeros[0])
print(numeros)

numeros[1] = 7
print(numeros)

numeros.sort()
print(numeros)


