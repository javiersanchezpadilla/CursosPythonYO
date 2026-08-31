""" Tipos de Argumentos:
Posicionales: El orden de los valores al llamar la función determina a qué parámetro corresponden.

"""
def dar_bienvenida(nombre, ciudad):
    print(f"Hola {nombre}, qué gusto verte desde {ciudad}.")


# El orden importa, esto es incorrecto, no marca error pero no cumple
dar_bienvenida("Acapulco", "Javier") 

# Nombrados (Keyword Arguments): Puedes indicar explícitamente el nombre del 
# parámetro al llamar a la función, lo que te permite cambiar el orden sin 
# romper la lógica.

dar_bienvenida(ciudad="Acapulco", nombre="Javier")  # Funciona correcto
dar_bienvenida(nombre="Javier", ciudad="Acapulco")  # Funciona correcto
dar_bienvenida("Javier", "Acapulco")                # Funciona correcto
