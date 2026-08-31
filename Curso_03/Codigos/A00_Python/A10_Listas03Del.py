""" INSTRUCCIÓN DEL

    La instrucción del en Python elimina elementos o secciones enteras de una 
    lista utilizando sus índices, y también puede borrar la variable por 
    completo de la memoria.
    
    Usos principales de deL
    ----------------------
    1)  Eliminar por índice: Borra un elemento específico indicando su 
        posición exacta.
    2)  Eliminar por rebanadas (slices): Borra múltiples elementos contiguos 
        al mismo tiempo de forma rápida.
    3)  Borrar la variable: Elimina la lista completa de la memoria, por lo 
        que la variable deja de existir.
        
    Diferencia con otros métodos
    ----------------------------
    **) Diferencia con .pop(): del solo borra el elemento; no te lo devuelve 
        como lo hace .pop().
    **) Diferencia con .remove(): del busca por posición (índice), mientras 
        que .remove() busca por el valor del elemento.
    **) Diferencia con .clear(): del lista[:] vacía la lista conservando la 
        variable, idéntico a .clear(), pero del lista destruye la variable 
        por completo.
"""
numeros = [10, 20, 30, 40, 50, 60]

# 1. Eliminar un solo elemento (el 30, índice 2)
del numeros[2]  # Resultado: [10, 20, 40, 50, 60]

# 2. Eliminar varios elementos (índices 1 y 2: el 20 y el 40)
del numeros[1:3]  # Resultado: [10, 50, 60]

# 3. Eliminar la variable de la memoria
del numeros
# print(numeros)  # Esto daría NameError porque la lista ya no existe
