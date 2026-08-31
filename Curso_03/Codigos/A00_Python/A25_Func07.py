""" ARGUMENTOS DINÁMICOS (*ARGS Y **KWARGS)

    Cuando no sabes de antemano cuántos argumentos le pasará el usuario a tu 
    función, Python ofrece dos mecanismos muy flexibles:

    *args (Tuple de argumentos posicionales): Captura cualquier cantidad de argumentos adicionales en una tupla.
    **kwargs (Diccionario de argumentos nombrados): Captura cualquier cantidad de argumentos adicionales en formato de diccionario (clave-valor).

"""
def sumar_todos(*args):
    # 'args' se comporta como una tupla (10, 20, 30, 40)
    return sum(args)

print(sumar_todos(10, 20))         # 30
print(sumar_todos(10, 20, 30, 40)) # 100


def mostrar_perfil(**kwargs):
    # 'kwargs' se comporta como un diccionario {'nombre': 'Javier', 'rol': 'Dev'}
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_perfil(nombre="Javier", rol="Estudiante", lenguaje="Python")
