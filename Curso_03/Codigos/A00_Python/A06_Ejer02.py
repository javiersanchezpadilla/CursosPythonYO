""" Crear un código que simule el funcionamiento de una máquina de cambio de divisas. Por el momento 
    nuestra máquina sólo recibe dólares y devuelve pesos.
    La máquina va a necesitar disponer de variables que le brinden la siguiente información:
    ** Nombre del usuario.
    ** Fecha en que se realiza la operación.
    ** Momento del día (día, tarde o noche).
    ** Cantidad de dólares a cambiar.

    Con todo eso, la máquina va a imprimir en pantalla (en diferentes líneas por supuesto) un 
    mensaje que incluya los siguientes
    Requisitos:
    Un saludo de bienvenida
    Información de la cantidad de dólares que va a entregar el usuario
    Información de la cantidad de euros que va a recibir
    Detalle específico de cuántos billetes de 200 pesos, 100 pesos, 50 pesos, 20 pesos, 
    monedas de 10, 5 y 1 peso, y el saldo en monedas que le serán entregados
    Un saludo de despedida
"""


# Encabezado con f-strings (PEP 8)
nombre = "Javier"
fecha = "16/08/2026"
saludo = "Buenos dias"

print(f"{saludo} {nombre}. Hoy es {fecha}. Bienvenido al Servicio de cambio de divisas\n")

dolares = 272.0
tipo_cambio = 19
pesos_a_recibir = int(dolares * tipo_cambio) # Convertimos a entero para trabajar con billetes

# Usamos una variable auxiliar para rastrear el dinero restante
sobrante = pesos_a_recibir

billetes_200 = sobrante // 200
sobrante %= 200  # Equivale a: sobrante = sobrante % 200

billetes_100 = sobrante // 100
sobrante %= 100

billetes_50 = sobrante // 50
sobrante %= 50

billetes_20 = sobrante // 20
sobrante %= 20

monedas_10 = sobrante // 10
sobrante %= 10

monedas_5 = sobrante // 5
sobrante %= 5

monedas_1 = sobrante  # Lo que queda son las monedas de $1

# Salida formateada
print(f"Cantidad en dólares: ${dolares:,.2f}")
print(f"Total en pesos:      ${pesos_a_recibir:,.2f}\n")

print(f"Billetes de 200: {billetes_200}")
print(f"Billetes de 100: {billetes_100}")
print(f"Billetes de 50:  {billetes_50}")
print(f"Billetes de 20:  {billetes_20}")
print(f"Monedas de 10:   {monedas_10}")
print(f"Monedas de 5:    {monedas_5}")
print(f"Monedas de 1:    {monedas_1}")