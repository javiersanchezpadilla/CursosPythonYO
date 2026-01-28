"""
Vas a crear un programa que le pida al usuario que ingrese un texto de 
al menos 10 palabras. Tu programa va a procesar ese texto, lo va a procesar,
 y le va a devolver un análisis detallado, que incluya:

Contar el número total de caracteres en el texto
Contar el número de caracteres sin incluir los espacios
Contar la cantidad de vocales que hay en el texto
Contar el número total de palabras en el texto ingresado

nota: para resolver los siguientes items, deberás investigar otros métodos 
de strings que no hemos visto. Recuerda valerte de type, dir y help
Eliminar la primera palabra
Reemplazar todos los espacios por guiones medios (-)
Cambia las mayúsculas a minúsculas y las minúsculas a mayúsculas
"""

frase = input("Proporcione una frase de al menos diez palabras: ")
print(frase)
                        # Contar el total de letras
total_letras = len(frase)
print('El total de caracteres de la cadena es {} '.format(total_letras))
                        # contar los caracteres sin espacios
espacios = frase.count(" ")
print(f'Total de espacios en blanco {espacios}')
letras_sin_espacios = total_letras - espacios
print(f'El total de letras sin espacios de la cadena es {letras_sin_espacios}')

                        # Contar las vocales de la palabra
vocal_a = frase.count("a")
vocal_e = frase.count("e")
vocal_i = frase.count("i")
vocal_o = frase.count("o")
vocal_u = frase.count("u")
total_vocales = vocal_a + vocal_e + vocal_i + vocal_o + vocal_u
print(f'El total de vocales de la frase es {total_vocales}')
                        # Contar el total de palabras
palabras = frase.count(" ") + 1
print(f'El total de palabras es {palabras}')

                        # Eliminar la primer palabra
ubicacion_primer_espacio = frase.find(" ")
print(ubicacion_primer_espacio)
frase_sin_primer_palabra = frase[ubicacion_primer_espacio + 1:]
print(frase_sin_primer_palabra)

                        # Reemplazar los espacios por guiones
nueva_frase = frase.replace(" ", "-")
print(nueva_frase)
                        # Cambiar las mayuscular por minusculas y visceversa
cambiar_mayus_mius = frase.swapcase()
print(cambiar_mayus_mius)
