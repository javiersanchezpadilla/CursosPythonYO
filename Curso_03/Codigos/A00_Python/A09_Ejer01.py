"""
Vas a crear un programa que le pida al usuario que ingrese un texto de 
al menos 10 palabras. Tu programa va a procesar ese texto, lo va a procesar,
 y le va a devolver un análisis detallado, que incluya:

Contar el número total de total_caracteres en el texto
Contar el número de total_caracteres sin incluir los espacios
Contar la cantidad de vocales que hay en el texto
Contar el número total de palabras en el texto ingresado

Reemplazar todos los espacios por guiones medios (-)
Cambia las mayúsculas a minúsculas y las minúsculas a mayúsculas
Eliminar la primer palabra del texto
"""
texto = input("Propocione un texto: ")

total_caracteres = len(texto)
total_espacios = texto.count(" ")

texto_minusculas = texto.lower()
total_vocales = texto_minusculas.count("a") + texto_minusculas.count("e") + \
                texto_minusculas.count("i") + texto_minusculas.count("o") + \
                texto_minusculas.count("u")
    
texto_sin_espacios = texto.strip()
total_palabras = texto_sin_espacios.count(" ") + 1
posicion_primer_espacio = texto_sin_espacios.strip().find(" ")


print('Total de total_caracteres:', total_caracteres)
print('Total de espacios:', total_espacios)
print('Total de caracteres', total_caracteres - total_espacios)
print('Total vocales:', total_vocales)
print('Total palabras:', total_palabras)
print(texto.replace(" ", "-"))
print(texto.swapcase())
print('Texto sin la primer palabra:', texto_sin_espacios[posicion_primer_espacio:])