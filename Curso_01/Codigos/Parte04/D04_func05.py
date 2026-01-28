# Funciones que llaman a otras funciones
def pedir_nombre():
    nombre = input('Dime tu nombre: ')
    return nombre

def pedir_apellido():
    apellido = input('Dime tu apellido: ')
    return apellido

def saludar():
    saludo = f'Hola {pedir_nombre()} {pedir_apellido()}'
    print(saludo)


saludar()

