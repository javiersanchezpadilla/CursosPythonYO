""" AGREGAR ELEMENTOS A UNA LISTA

    Para agregar varios elementos a una lista en Python en una sola 
    instrucción usando el método .extend(), la suma de listas con +, o la 
    asignación con rebanadas (slicing).
    
    Métodos para agregar varios elementos
    -------------------------------------
    A)  Método .extend(): Agrega los elementos de un iterable al final de la 
        lista original de forma directa.
    B)  Operador +: Crea una nueva lista sumando los elementos de ambas listas.
    C)  Rebanadas [:]: Permite insertar varios elementos en una posición 
        específica o al final modificando la lista.
        
    Ejemplos de uso
    ---------------
    **) Usar .extend(): mi_lista.extend([4, 5, 6]) modifica la lista actual 
        agregando los elementos al final.
    **) Usar +: nueva_lista = mi_lista + [4, 5, 6] junta las listas y guarda 
        el resultado en una variable nueva.
    **) Usar append() con cuidado: Si usas mi_lista.append([4, 5, 6]), 
        agregarás la lista entera como un solo elemento (una sublista), no los 
        elementos sueltos.
"""
a = [1, 2, 3, 4, 5, 4, 4, 4, 4]
b = ['a', 'b', 'c']

z = a[::] + b[1:]

print(a)
a.append(6)
a.append(7)
print(a)

a.extend(b)
print(a)

c = a + b
print(c)

a.append(b)
print(a)
print(z)
a.clear()   # elimina el contenido de la lista (no la lista)
# print('El valor 4 se cuentra en la posición', a.index(4))
print(a)
