palabra = "Hola a todos"
print(palabra)
print(palabra[0])
print(palabra[1])
print(palabra[2])
print('\nAcceder mediante valores negativos')
print(palabra[-1])
print(palabra[-2])
print(palabra[-3])
print(palabra[-4])
print('\nObteniendo segmentos de cadena')
print(palabra[0:4])     # El último valor no es incluyente
print(palabra[:4])      # El último valor no es incluyente
print(palabra[:40])     # No importa que nos pasemos
# imprimir desde el inicio hasta el final saltando de dos en dos
print(palabra[0:10:2])
print(palabra[0:10:2].upper())
print(palabra[::-1])
