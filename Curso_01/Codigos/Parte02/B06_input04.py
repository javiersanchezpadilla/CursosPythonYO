"""
    Desarrolla un programa que le pregunte al usuario la cantidad de 
    kilómetros que desea convertir a millas.
    Utiliza la función input() para recoger esta información, conviértela 
    a un valor numérico y realiza la conversión (considera que 1 kilómetro 
    equivale a 0.621371 millas). Finalmente, imprime el resultado.
    Instrucciones:
    Al iniciar el programa, debes pedir al usuario que ingrese una cantidad 
    de kilómetros utilizando la orden siguiente: "Introduce la cantidad de 
    Kilómetros recorridos: "  y almacenar esta entrada en una variable llamada km
    Luego, convierte los kilómetros a millas considerando que 1 kilómetro 
    equivale a 0.621371 millas  y guarda el resultado.
    Finalmente, imprime el resultado de esta operación.
"""

km = int(input("Introduce la cantidad de Kilómetros recorridos: "))
print(km * 0.621371) 