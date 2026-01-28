"""
    Escribe un programa que tenga dos variables de tipo string palabra y 
    letra.   Almacena una palabra y una letra de tu elección. Utiliza el 
    método adecuado para contar cuántas veces aparece la letra en la variable palabra.
"""

palabra = 'Hola a todos hoy es martes 21 de enero de 2025'
letra = 'a'
print(palabra.count(letra))
print(f'El numero de repeticiones de la letra "{letra}" en la cadena es {palabra.count(letra)}')
