"""
Dada una lista de amigos amigos = ["Juan", "Ana", "Laura"], 
escribe un programa donde definas una variable llamada nombre y 
coloques un nombre de tu elección. Si el nombre está en la lista amigos, 
el programa debe imprimir "{nombre} está en mi grupo de amigos", 
reemplazando  con el nombre ingresado por el usuario. Si el nombre no 
está en la lista, el programa no debe imprimir nada.
"""

amigos = ["Juan", "Ana", "Laura"]
nombre = 'Javier'
if nombre in amigos:
    print(f"{nombre} está en mi grupo de amigos")
