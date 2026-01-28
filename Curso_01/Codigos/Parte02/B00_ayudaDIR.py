""" PAra pedir ayudas podemos hacerlo de dos maneras 
    dir() en Python es una función incorporada que se utiliza para inspeccionar objetos, 
    devolviendo una lista de sus atributos y métodos. Se usa con dir(objeto) para ver 
    las propiedades de un objeto específico o solo dir() para obtener una lista de los 
    nombres disponibles en el espacio de nombres actual. Es una herramienta útil para la 
    exploración y depuración, ya que ayuda a descubrir las capacidades de un objeto sin 
    necesidad de consultar la documentación
    Para qué sirve
    Descubrir propiedades: Permite ver qué métodos y atributos están disponibles para un 
    objeto. 
    Explorar módulos y bibliotecas: Es muy útil para entender las funciones de un nuevo 
    módulo sin necesidad de buscar en la documentación externa. 
    Depurar: Ayuda a identificar los nombres y estructuras de los objetos durante la 
    depuración del código. . 
"""

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre}"


persona1 = Persona("Ana")
# La salida son todos los metodos disponibles de la clase mas los que nosotros definimos
print(dir(persona1))

cadena = "hola"
# Para visualizar los metodos y atributos disponibles para un objeto
print(dir(cadena))

 
