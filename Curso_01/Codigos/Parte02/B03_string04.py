"""
    Crea un programa que tome la frase "Python es divertido" y realice 
    las siguientes operaciones en orden, utilizando métodos de string 
    correspondientes: 
    1. Remplaza la palabra "divertido" por la palabra "genial". 
       Deberás investigar cuál método de string sirve para reemplazar una 
       palabra por otra. Puedes hacerlo con el método dir().
    2. Almacena el resultado en una variable llamada frase_modificada
    3. Imprime el resultado en pantalla.
"""

frase = "Python es divertido"
frase_modificada = frase.replace('divertido', 'genial')
print(frase_modificada)
