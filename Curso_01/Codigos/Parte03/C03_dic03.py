"""
Dado el siguiente diccionario edades, que asocia nombres de personas 
con su edad: edades = {"Juan": 28, "Elena": 32, "Marcos": 17}
Realiza las siguientes tareas: 
Accede a la edad de Elena e imprímela.
Modifica la edad de Juan a 29 años e imprime el resultado.
Añade un nuevo par clave-valor, asociando a "Luisa" con 25 años e 
imprime el diccionario completo actualizado.
"""

edades = {"Juan": 28, "Elena": 32, "Marcos": 17}
print(edades["Elena"])
edades["Juan"] = 29
print(edades["Juan"])
edades["Luisa"] = 25
print(edades)

