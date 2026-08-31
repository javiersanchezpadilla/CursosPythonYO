""" FORMATO DE NÚMEROS

        {variable : [relleno][alineación][ancho][separador][.precisión][tipo]}

    No necesitas aprenderte todos de memoria. Los más usados siempre
    serán .2f (dinero/ciencias/Contabilidad) y %d/%m/%Y (fechas).

    Sistemas Numéricos
    ------------------
    Para convertir números a otras bases, es muy fácil:

        *) b    Binario.
        *) x    Hexadecimal.
        *) o    Octal.
"""
numero = 25
print(f"Binario: {numero:b}")  # 11001
print(f"Hex: {numero:x}")      # 19
print(f"El valor {numero} es binario={numero:b}, hexadecimal={numero:x}, octal={numero:o}")