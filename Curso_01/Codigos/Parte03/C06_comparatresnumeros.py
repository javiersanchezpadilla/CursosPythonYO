num1 = 2
num2 = 3
num3 = 1

menor = None
medio = None
mayor = None

# Buscamos al menor de los tres
if num1 <= num2 and num1 <= num3:
  menor = num1
elif num2 <= num1 and num2 <= num3:
  menor = num2
else:
  menor = num3

# Ahora buscamos al mayor (este se resolvio en clase)
if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3

# Por diferencia obtenemos el medio
medio = num1 + num2 + num3 - menor - mayor

# Imprimimos los resultados
print("El orden de los números es:")
print("Menor:", menor)
print("Medio:", medio)
print("Mayor:", mayor)
