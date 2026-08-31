""" EJERCICIO SOBRE EL USO DE FUNCIONES

    El ejercicio simula un sistema real de comercio electrónico. Obliga a los 
    alumnos a dividir un problema grande en partes pequeñas (funciones) y 
    promueve las buenas prácticas de programación.

    Título del Ejercicio:
    ---------------------
    Sistema de Cotización de Envíos y Descuentos

    Objetivo Académico:
    -------------------
    Diseñar un programa modular en Python que calcule el costo total de una 
    compra en línea considerando:

    1)  El cálculo de impuestos.
    2)  El procesamiento de cupones de descuento.
    3)  El cálculo de costo de envío según la distancia.
    4)  La generación de un resumen formateado para el cliente.

    Instrucciones para los Alumnos
    ------------------------------
    Escribe un programa que contenga las siguientes 4 funciones independientes 
    y un bloque principal de ejecución:

    1. calcular_impuesto(subtotal, porcentaje_impuesto=16)
    Propósito: Calcular el monto correspondiente a impuestos (por ejemplo, IVA).
    Parámetros:
        subtotal (float): El costo base de los productos.
        porcentaje_impuesto (float, opcional): Por defecto debe ser 16.
    Retorno: El valor numérico del impuesto calculado (float).

    2. aplicar_cupon(subtotal, codigo_cupon)
    Propósito: Determinar el descuento aplicable según una clave.
    Parámetros:
        subtotal (float).
        codigo_cupon (str).
    Lógica:
        Si el cupón es "DESCUENTO10", aplica un 10% de descuento.
        Si el cupón es "SUPER20", aplica un 20% de descuento.
        Si el cupón no es válido o está vacío, el descuento es 0.
    Retorno: El monto del descuento en dinero (float).

    3. calcular_envio(distancia_km, envio_prioritario=False)
    Propósito: Calcular la tarifa de entrega.
    Lógica:
        La tarifa base es de $50.00 pesos.
        Se suman $5.00 pesos adicionales por cada kilómetro recorrido.
        Si envio_prioritario es True, se le suma un recargo de $100.00 pesos.
        Retorno: El costo total del envío (float).

    4. generar_ticket(nombre_cliente, subtotal, descuento, impuesto, envio)
    Propósito: Imprimir un desglose limpio y bien formateado usando f-strings.
    Retorno: No retorna nada (None), solo imprime en pantalla.
"""

def calcular_impuesto(subtotal, porcentaje_impuesto=16):
    """Calcula el monto de impuesto sobre un subtotal."""
    return subtotal * (porcentaje_impuesto / 100)


def aplicar_cupon(subtotal, codigo_cupon=""):
    """Determina el descuento aplicable según el cupón ingresado."""
    codigo = codigo_cupon.upper().strip()
    if codigo == "DESCUENTO10":
        return subtotal * 0.10
    elif codigo == "SUPER20":
        return subtotal * 0.20
    else:
        return 0.0


def calcular_envio(distancia_km, envio_prioritario=False):
    """Calcula el costo del envío según la distancia y la modalidad."""
    costo_base = 50.0 + (distancia_km * 5.0)
    if envio_prioritario:
        costo_base += 100.0
    return costo_base


def generar_ticket(nombre_cliente, subtotal, descuento, impuesto, envio):
    """Muestra un resumen formateado de la transacción."""
    total_final = (subtotal - descuento) + impuesto + envio
    
    print("\n" + "="*40)
    print(f"     RESUMEN DE COMPRA: {nombre_cliente.upper()}")
    print("="*40)
    print(f"Subtotal productos : ${subtotal:,.2f}")
    print(f"Descuento aplicado : -${descuento:,.2f}")
    print(f"Impuestos (16%)    : ${impuesto:,.2f}")
    print(f"Costo de envío     : ${envio:,.2f}")
    print("-" * 40)
    print(f"TOTAL A PAGAR      : ${total_final:,.2f}")
    print("="*40 + "\n")


# --- BLOQUE PRINCIPAL DE PRUEBA ---
if __name__ == "__main__":
    # Datos de entrada de prueba
    cliente = "Javier"
    compra = 1500.0
    cupon = "SUPER20"
    distancia = 12.5
    es_expres = True

    # Flujo ejecutable invocando a las funciones
    monto_descuento = aplicar_cupon(compra, cupon)
    monto_impuesto = calcular_impuesto(compra - monto_descuento)
    monto_envio = calcular_envio(distancia, envio_prioritario=es_expres)

    generar_ticket(cliente, compra, monto_descuento, monto_impuesto, monto_envio)
