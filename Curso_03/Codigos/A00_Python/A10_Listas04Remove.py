""" EL MÉTODO .REMOVE() 

    elimina el primer elemento de la lista que coincida con el valor 
    específico que le pases como argumento.
    
    Características clave
    ---------------------
    **) Busca por valor: No utiliza índices (posiciones); busca directamente 
        el contenido del elemento.
    **) Elimina solo la primera coincidencia: Si el elemento aparece varias 
        veces, solo borra el primero que encuentra (de izquierda a derecha).
    **) Modifica la lista original: Cambia la lista directamente y no devuelve 
        ningún valor (None).
    **) Lanza un error si no existe: Si el valor no está en la lista, el 
        programa se detiene con un error de tipo ValueError
"""
animales = ["perro", "gato", "león", "gato", "oso"]

# Eliminar el primer "gato"
animales.remove("gato")

print(animales)  # Resultado: ['perro', 'león', 'gato', 'oso']

# Cómo evitar errores si el elemento no existe
# --------------------------------------------
# Para evitar que tu programa falle (ValueError) si no estás seguro de que el 
# elemento está en la lista, es una buena práctica verificarlo primero con la 
# palabra clave in:
# Verificar antes de borrar
if "gato" in animales:
    animales.remove("gato")
else:
    print("El gato no está en la lista.")
