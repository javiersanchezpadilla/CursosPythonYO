"""
    Escribir un programa que solicite al usuario su año de nacimiento 
    (almacena esta entrada en una variable llamada nacimiento ), realiza 
    una operación matemática simple con este valor y muestra el resultado. 
    Este ejercicio tiene como objetivo practicar la entrada de datos por 
    parte del usuario, la conversión de tipos de datos y la realización de 
    operaciones matemáticas básicas.
    Instrucciones:
    Al iniciar el programa, debes pedir al usuario que ingrese el año en 
    que nació utilizando la pregunta: "¿En qué año naciste?" . y almacenar 
    esta entrada en una variable llamada nacimiento
    Una vez recibido el año de nacimiento como entrada, debes convertir este 
    valor de una cadena de texto (str) a un número entero (int). Sobre escribe 
    la variable  nacimiento sin crear nuevas variables.
    Luego, suma 1 al año de nacimiento convertido y guarda el resultado. Sobre 
    escribe la variable  nacimiento sin crear nuevas variables.
    Finalmente, imprime el resultado de esta operación.
"""
nacimiento = input("¿En qué año naciste? ")
nacimiento = int(nacimiento) + 1
print(nacimiento) 