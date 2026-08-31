""" RETORNAR MÚLTIPLES VALORES

    A diferencia de otros lenguajes, en Python una función puede retornar 
    varios valores a la vez. Internamente, Python los empaqueta y devuelve 
    dentro de una tupla (realmente es un solo valor)
"""
def obtener_estadisticas_basicas(numeros):
    suma = sum(numeros)
    promedio = suma / len(numeros)
    # Devuelve una tupla (suma, promedio)
    return suma, promedio  

# Desempaquetado directo de los valores
total_suma, promedio_val = obtener_estadisticas_basicas([10, 20, 30, 40])
print(f"Suma: {total_suma}, Promedio: {promedio_val}")