""" AMBITO O ALCANCE DE VARIABLES (SCOPE)

    Las variables creadas dentro de una función tienen un alcance local: 
    existen únicamente durante la ejecución de esa función y se destruyen al 
    finalizar.
"""
variable_global = "Soy accesible desde cualquier lado"

def mi_funcion():
    variable_local = "Solo existo dentro de la función"
    print(variable_global)              # correcto
    print(variable_local)               # correcto

mi_funcion()


# si intento acceder a la variable creada dentro de la variable se ontendra
# un error
# print(variable_local) # <--- Lanza un NameError
