""" DICCIONARIOS

    Un diccionario en Python (tipo de dato dict) es una estructura de datos 
    nativa que almacena información en forma de pares clave: valor (key-value)
    Si en una lista o tupla accedes a los elementos a través de un índice 
    numérico por su posición (lista[0]), en un diccionario accedes a la 
    información a través de una clave personalizada (por ejemplo, 
    usuario["nombre"]).
    
    Características Principales
    ---------------------------
    1)  Estructura Clave-Valor: Cada dato (valor) está asociado a una etiqueta
        única (clave).
    2)  Claves Únicas: No puede haber claves duplicadas. Si asignas un valor a 
        una clave que ya existe, el valor anterior se sobrescribe.
    3)  Claves Inmutables: Las claves deben ser de un tipo de dato inmutable 
        (str, int, float, tuple). Las cadenas de texto (str) son las más 
        comunes.
    4)  Mutables: Puedes agregar, modificar o eliminar pares clave-valor 
        después de crear el diccionario.
    5)  Búsqueda Ultra Rápida: Al igual que los conjuntos (set), los 
        diccionarios utilizan tablas hash, por lo que buscar un elemento por 
        su clave toma tiempo constante O(1)
"""
# Creación de un diccionario
usuario = {
    "nombre": "Pedro",
    "edad": 25,
    "ciudad": "Acapulco",
    "cursos": ["Python", "Pandas", "Django"]
}

# Acceso directo por clave
print(usuario["nombre"])  # Salida: Javier

# Modificar o agregar un valor
usuario["edad"] = 26               # Modifica el valor existente
usuario["profesion"] = "Ingeniero"  # Agrega una nueva clave-valor

# PARA OBTENER INFORMACIÓN DE FORMA SEGURA
#  .get(clave, valor_por_defecto)
# Permite consultar un valor de forma segura. Si la clave no existe, en lugar 
# de lanzar un KeyError, devuelve None (o el valor alternativo que tú 
# especifiques).
# La clave 'email' no existe
email = usuario.get("email", "Correo no registrado")
print(email)  # Salida: Correo no registrado

# Para Eliminar Elementos
# .pop(clave, valor_por_defecto)
# Elimina la clave especificada y devuelve el valor que contenía. Si no la 
# encuentra, devuelve el valor por defecto provisto.
edad_eliminada = usuario.pop("edad")
print(f"Se eliminó la edad: {edad_eliminada}")
print(usuario)

# .popitem()
# Elimina y devuelve el último par (clave, valor) insertado en el diccionario 
# (sigue la regla LIFO - Last In, First Out).
ultimo_par = usuario.popitem()
print(f"Se eliminó: {ultimo_par}")  # Salida: ('profesion', 'Ingeniero')
print(usuario)

# .clear()
# Elimina todos los elementos, dejando el diccionario totalmente vacío {}
# usuario.clear()
# print(usuario)

# Para Combinar o Copiar Diccionarios
# .update(otro_diccionario)
# Actualiza el diccionario agregando los pares del nuevo diccionario. 
# Si alguna clave ya existía, sobrescribe su valor.
nuevos_datos = {"ciudad": "Acapulco", "nivel": "Avanzado"}

usuario.update(nuevos_datos)
# 'ciudad' se actualiza y 'nivel' se agrega como clave nueva
print(usuario)

