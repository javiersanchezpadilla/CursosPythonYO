"""
Escribe un programa que itere sobre una lista de cadenas que representan 
nombres de paises por ejemplo: ['Francia', 'Alemania', 'España', 'Italia', 
'Portugal', 'Chile']. Dentro del bucle, usa una declaración if para imprimir 
el nombre del país solo si contiene la letra 'a'.
Asegurate que tu lista tenga por nombre: paises
Podrás agregar o eliminar los paises que desees a la lista paises proporcionada inicialmente.
"""

paises = ['Francia', 'Alemania', 'España', 'Italia', 'Portugal', 'Chile', 'Mexico']

for pais in paises:
    if pais.count('a') > 0:
        print(pais)