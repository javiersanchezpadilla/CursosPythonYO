""" SLICING (REBANAR)

    El slicing (o rebanado) es una técnica de Python que te permite extraer 
    una subcadena (o porción) de una cadena de texto principal utilizando 
    corchetes [...].1. La Sintaxis BásicaLa sintaxis fundamental del slicing 
    acepta hasta tres parámetros dentro de los corchetes, separados por dos 
    puntos :: 
    
                cadena[ inicio : fin : paso ]
        
    1)  inicio: El índice donde comienza la extracción (incluido).
    2)  fin: El índice donde termina la extracción (excluido — se detiene 
        justo antes).
    3)  paso: (Opcional) Indica el tamaño del salto entre cada carácter (por 
        defecto es 1)
        
    Índices Positivos y Negativos en Python
    ---------------------------------------
    Para usar slicing de forma ágil, recuerda que los caracteres de un texto 
    se pueden direccionar de dos formas:
    
        Texto:       P    y    t    h    o    n
        Positivos:   0    1    2    3    4    5
        Negativos:  -6   -5   -4   -3   -2   -1

    Expresión   	Qué hace
    ------------------------------------------------------
    s[a:b]      	Del índice a hasta antes del índice b
    s[:b]       	Desde el inicio hasta antes de b
    s[a:]	        Desde a hasta el final
    s[-a:]      	Los últimos a caracteres del texto
    s[::-1]	        Devuelve la cadena invertida
"""

texto = "Python"

# A. Especificando inicio y fin
# -----------------------------
# Del índice 0 al 4 (el 4 'h' NO se incluye)
print(texto[0:4])   # Salida: 'Pyth'

# Del índice 2 al 5
print(texto[2:5])   # Salida: 'tho'

# B. Omitiendo inicio o fin (Atajos)
# ----------------------------------
# Si dejas en blanco un valor, Python asume los límites del texto por defecto:
# Si omites 'inicio', empieza desde el principio (índice 0)
print(texto[:4])    # Salida: 'Pyth'

# Si omites 'fin', llega hasta el final de la cadena
print(texto[2:])    # Salida: 'thon'

# Si omites ambos, copia la cadena completa
print(texto[:])     # Salida: 'Python'
