""" BUENAS PRÁCTICAS AL ESCRIBIR FUNCIONES (PEP 8)

    1)  Responsabilidad Única: Cada función debe hacer una sola cosa y hacerla 
        bien.
    2)  Nombres Descriptivos: Usa verbos en minúscula para nombrarlas 
        (calcular_promedio(), obtener_usuario()).
    3)  Docstrings: Documenta qué hace tu función, sus parámetros y lo que 
        retorna utilizando triples comillas dentro de la primera linea

"""

def calcular_descuento(precio, porcentaje=10):
    """Calcula el precio final aplicando un porcentaje de descuento.

    Args:
        precio (float): El valor original del producto.
        porcentaje (float, opcional): Porcentaje a descontar. Por defecto es 10.

    Returns:
        float: El nuevo precio con el descuento aplicado.
    """
    return precio * (1 - porcentaje / 100)