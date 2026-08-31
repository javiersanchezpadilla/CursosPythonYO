""" VARIABLES GLOBALES DENTRO DE FUNCIONES

    Mientras no intente modificar el valor de la variable global dentro de la 
    función, Python asume que es una variable global, pero en el momento que
    intente hacer una operación se asume como local

    ERROR 1
    --------------------------------------------------------------------------
    variable_global = 100

    def mi_funcion():
        print(variable_global)
        variable_global += 1000     <-- Busca como variable local y marca error
        print(variable_global)          ya que no esta inicializada

    print(variable_global)
    mi_funcion()
    print(variable_global)
    
    
    ERROR 2     Salida 100   0   1000   100
    --------------------------------------------------------------------------
    variable_global = 100

    def mi_funcion():
        variable_global = 0         <-- la trata como una variable local
        print(variable_global)          si declaro la variable dentro de la 
        variable_global += 1000         función la tratara como local
        print(variable_global)

    print(variable_global)
    mi_funcion()
    print(variable_global)
"""


variable_global = 100

def mi_funcion():
    global variable_global          # <-- Solución decirle a Python que es una
    print(variable_global)          #     variable global
    variable_global += 1000
    print(variable_global)

print(variable_global)
mi_funcion()
print(variable_global)
