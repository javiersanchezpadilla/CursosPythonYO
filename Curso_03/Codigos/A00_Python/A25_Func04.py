""" VALORES POR DEFECTO (PARÁMETROS OPCIONALES)

    Puedes asignar un valor predeterminado a un parámetro por si el usuario no 
    lo proporciona al ejecutarla.
"""
def saludar_usuario(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}!")

def mi_funcion(a=1, b=2, c=3):
    print('El primer argumenro es', a)
    print('El segunfo argumento es', b)
    print('El tercer argumento es', c)


saludar_usuario("Javier")                   # Imprime: Hola, Javier!
saludar_usuario("Javier", "Buenos días")    # Imprime: Buenos días, Javier!


print('\nForma normal y tradicional de llamar a la función')
mi_funcion(10, 20 ,30)

print('\nForma alternativa de llamar especificando el parametro')
mi_funcion(c=30, a=10, b=20)

print('\nllamando con solo dos argumentos')
mi_funcion(10, 1000)

print('\nLlamando con solo un argumento')
mi_funcion(1)

print('\nLlamando la función sin argumentos')
mi_funcion()