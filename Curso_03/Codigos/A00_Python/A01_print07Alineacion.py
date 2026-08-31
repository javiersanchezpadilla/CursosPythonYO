""" Alineación y Relleno: El decorador de interiores

    A veces quieres que los datos se vean como una tabla perfecta en la 
    consola
    
    {variable : [relleno][alineación][ancho][separador][.precisión][tipo]}
    
    Usamos los símbolos <, >, y ^ para indicar la alineación

        *) <    Alinea a la izquierda (por defecto para texto).
        *) >    Alinea a la derecha (por defecto para números).
        *) ^    Centra el contenido.
"""

texto = "HOLA"
print(f"|{texto:<10}|")  # |HOLA      | (10 espacios total)
print(f"|{texto:>10}|")  # |      HOLA|
print(f"|{texto:^10}|")  # |   HOLA   |

# Puedes rellenar los espacios vacíos con un carácter:
print(f"{texto:=^20}")   # ========HOLA========