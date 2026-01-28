"""
Crea dos listas: lista1 con los elementos 1, 2, 3, y lista2 con los elementos 4, 5, 6.
Concatena lista1 y lista2 para formar una nueva lista llamada combinada. 
Imprime combinada.
Multiplicación de Listas  Utiliza la lista lista1 y multiplica su contenido por 
3 para crear una nueva lista llamada repetida. Esto hará que los elementos de 
lista1 se repitan tres veces en repetida. Imprime la lista repetida.
Creación de Sublistas:  A partir de la lista combinada creada en el paso 2, 
crea una sublista llamada sublista que contenga solo los elementos desde el 
índice 1 hasta el índice 4 (sin incluir el elemento en el índice 4). Imprime sublista.
"""

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
combinada = lista1 + lista2
print(combinada)
repetida = lista1 * 3
print(repetida)
sublista = combinada[1:4]
print(sublista)