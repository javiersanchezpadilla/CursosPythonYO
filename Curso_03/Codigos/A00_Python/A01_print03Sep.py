""" Ajustes de estilo

    sep Funciona SOLO CUANDO USAMOS print e indicamos lo elementos a unir
    con comas (,).

    sep (separador de palabras)

    A) Por defecto Python deja un espacio pequeño entre cada palabra.
    B) Con sep: Tú decides qué poner entre ellos. ¿Quieres que estén pegados? 
    ¿Quieres poner una valla? ¿Un guion?

    Muy importante!!!: sep define qué carácter se coloca entre los elementos 
    que separas por comas.
"""

# Es como pegamento pero con palabras
print('Imprimiendo una cadena compuesta\n')

print('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
print('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', sep='')
print('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', sep='*')
print('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', sep='-')
print('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', sep='😀')