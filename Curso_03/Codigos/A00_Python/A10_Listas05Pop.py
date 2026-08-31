""" EL MÉTODO .POP() 

    Elimina y devuelve un elemento de la lista. Por defecto, elimina el último 
    elemento, pero puedes pasarle un índice para eliminar un elemento en una 
    posición específica.
    
    Características clave
    ---------------------
    1)  Extrae el elemento: A diferencia de del o .remove(), .pop() saca el 
        elemento para que puedas guardarlo en una variable o usarlo de inmediato.
    2)  Modifica la lista original: Reduce el tamaño de la lista de forma 
        directa.
    3)  Índice por defecto: Si no le pasas ningún argumento, asume que quieres 
        eliminar el último elemento (índice -1).
    4)  Lanza un error si está vacía o el índice no existe: Si intentas usarlo 
        en una lista vacía o con un índice fuera de rango, dará un error de 
        tipo IndexError
"""
lenguajes = ["Python", "Java", "C++", "JavaScript"]

# 1. Usar pop() sin argumentos (elimina el último)
ultimo = lenguajes.pop()
print(ultimo)     # Resultado: 'JavaScript'
print(lenguajes)   # Resultado: ['Python', 'Java', 'C++']

# 2. Usar pop() con un índice específico (elimina 'Java' en el índice 1)
segundo = lenguajes.pop(1)
print(segundo)    # Resultado: 'Java'
print(lenguajes)   # Resultado: ['Python', 'C++']
