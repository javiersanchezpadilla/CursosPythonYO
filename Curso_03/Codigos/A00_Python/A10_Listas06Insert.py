""" METODO .insert()

    El método .insert() te permite agregar un elemento en una posición 
    (índice) específica de la lista, desplazando los elementos siguientes 
    hacia la derecha.
    
    Características clave
    ---------------------
    **) Requiere dos argumentos: lista.insert(índice, elemento), el primer 
        valor es la posición donde quieres colocarlo y el segundo es el 
        objeto que vas a guardar.
    **) No sobreescribe: No borra el elemento que ya estaba en esa posición, 
        sino que "lo empuja" hacia adelante.
    **) Modifica la lista original: Cambia la lista directamente en memoria y 
        devuelve None.
    **) Manejo de índices fuera de rango: Si el índice es más grande que el 
        tamaño de la lista, lo agrega al final (como .append()). Si es un 
        número negativo muy grande, lo agrega al inicio.

"""
colores = ["rojo", "azul", "verde"]

# 1. Insertar en una posición intermedia (índice 1)
colores.insert(1, "amarillo")
print(colores)  # Resultado: ['rojo', 'amarillo', 'azul', 'verde']

# 2. Insertar al principio de la lista (índice 0)
colores.insert(0, "negro")
print(colores)  # Resultado: ['negro', 'rojo', 'amarillo', 'azul', 'verde']
