""" OPERADORES COMPUESTOS, OPERADORES DE ASIGNACIÓN COMPUESTA U 
    OPERADORES DE ASIGNACIÓN AUMENTADA.

    Aunque el nombre técnico más común en programación es operadores de 
    asignación compuesta (o también conocidos como operadores de asignación 
    aumentada).
    Se llaman así porque combinan dos acciones en un solo paso:
    Realizan una operación matemática (suma, resta, potencia, etc.).
    Hacen la asignación (guardan el resultado en la misma variable).
    
    La forma larga:
    ---------------
    puntos = 10
    puntos = puntos + 5  # "Puntos ahora es igual a lo que había antes más 5"
    
    La forma con operador compuesto:
    --------------------------------
    puntos = 10
    puntos += 5          # "Súmale 5 a los puntos"
    
    Tabla de las asignaciones
    -------------------------
    Operador    Nombre                          Ejemplo     Equivalente a.
    ----------------------------------------------------------------------
    +=          Suma y asigna                   x += 3      x = x + 3
    -=          Resta y asigna                  x -= 2      x = x - 2
    *=          Multiplica y asigna             x *= 4      x = x * 4
    **=         Potencia y asigna               x **= 2     x = x ** 2
    //=         División entera y asigna        x //= 3     x = x // 3
    %=          Residuos (módulo) y asigna      x %= 2      x = x % 2
    
    Un detalle importante con //= y %=
    Estos dos son muy útiles cuando trabajas con lógica de aplicaciones:

    //=     Úsalo cuando quieres dividir pero descartar los decimales (solo 
            quieres el número entero).
    %=      Úsalo para saber qué "sobró" de una división. Es el truco clásico 
            para saber si un número es par o impar dentro de una función lambda
            como las que vimos antes.
    
    notas importantes para no olvidar:
    El orden de los símbolos importa: Siempre va primero el símbolo matemático 
    y luego el igual (+=). Si lo pones al revés (=+), Python pensará que estás 
    intentando asignar un número positivo, por ejemplo: x = +5.

    Tipo de dato en la división: Nota que al usar /=, el resultado automáticamente
    se convierte en un número decimal (float), mientras que con //= se mantiene 
    como entero (int) si los números originales eran enteros.
"""

# Empezamos con una cantidad base
cantidad = 10

# 1. += (Suma y asigna)
# Llega un nuevo pedido de 5 dulces.
cantidad += 5  # Es igual a: cantidad = 10 + 5
print(f"Suma (+=): Ahora hay {cantidad} dulces.") # 15

# 2. -= (Resta y asigna)
# Vendemos 3 dulces.
cantidad -= 3  # Es igual a: cantidad = 15 - 3
print(f"Resta (-=): Quedan {cantidad} dulces.") # 12

# 3. *= (Multiplica y asigna)
# ¡Promoción! Duplicamos el inventario por temporada.
cantidad *= 2  # Es igual a: cantidad = 12 * 2
print(f"Multiplicación (*=): Inventario duplicado a {cantidad}.") # 24

# 4. /= (Divide y asigna)
# Decidimos repartir los dulces en 2 cajas iguales.
cantidad /= 2  # Es igual a: cantidad = 24 / 2
print(f"División (/=): Cada caja tiene {cantidad} dulces.") # 12.0

# 5. //= (División Entera y asigna)
# Queremos repartir 12 dulces entre 5 niños, pero solo dulces completos.
cantidad //= 5  # Es igual a: cantidad = 12 // 5
print(f"División Entera (//=): Cada niño recibe {cantidad} dulces completos.") # 2

# 6. %= (Módulo/Residuo y asigna)
# Teníamos 12 dulces, dimos 2 a cada uno de los 5 niños (10 en total).
# ¿Cuántos sobraron en la bolsa?
sobrante = 12
sobrante %= 5  # Es igual a: sobrante = 12 % 5
print(f"Residuo (%=): Sobraron {sobrante} dulces en la bolsa.") # 2

# 7. **= (Potencia y asigna)
# El crecimiento de ventas es exponencial. Elevamos 3 al cuadrado.
ventas_potenciales = 3
ventas_potenciales **= 2  # Es igual a: ventas_potenciales = 3 * 3
print(f"Potencia (**=): El crecimiento proyectado es de {ventas_potenciales}.") # 9
