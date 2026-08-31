""" RETORNO DE VALORES (RETURN)

    Una función no solo realiza acciones; frecuentemente necesita procesar 
    información y devolver un resultado al resto del programa mediante la 
    instrucción return.
    
    Nota: Si una función no incluye una instrucción return, Python devolverá 
    implícitamente el valor especial None.
"""
def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area  # Devuelve el valor numérico al llamador

# Guardamos el resultado en una variable
resultado = calcular_area_rectangulo(5, 3)
print(f"El área del rectángulo es: {resultado}") # 15

# Si usamos f-string podemos directamente referenciar la funcion
print(f"El área del rectángulo es: {calcular_area_rectangulo(10, 10)}") 
