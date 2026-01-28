"""
Crea un programa donde declares una variable llamada edad, podrás 
inicializarla con el valor entero de tu preferencia. El programa 
debe imprimir "Tienes {edad} años, eres mayor de edad" si el usuario 
tiene 18 años o más, y "Tienes {edad} años, eres menor de edad" si 
tiene menos de 18 años.
"""

edad = 17
if edad >= 18:
    print(f"Tienes {edad} años, eres mayor de edad")
else:
    print(f"Tienes {edad} años, eres menor de edad")