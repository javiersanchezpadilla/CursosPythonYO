"""
Imagina que estás construyendo un sistema para una tienda.
Crea un programa que defina tres variables: producto, cantidad 
y precio. (asignándoles los valores que desees). Usa un f-string 
o cadena literal para imprimir una frase que describa cuántas 
unidades del producto hay y cuál es su precio total.
Por ejemplo, si producto es "manzanas", cantidad es 10, y precio es 0.30, 
tu programa debe imprimir "Hay 10 manzanas con un precio total de 3.0".
Recuerda multiplicar cantidad por precio para hallar el precio total.
"""
producto = 'Manzana'
cantidad = 10
precio = 0.5
print(f'Hay {cantidad} {producto} con un precio total de {cantidad * precio}')