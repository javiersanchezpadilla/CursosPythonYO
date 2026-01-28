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

nombre = "Javier"
fecha = "30/08/2025"
saludo = "Buenos dias"

bienvenida = saludo + " " + nombre + " Hoy es " \
             + fecha + ". Bienvenido al Servicio de cambio de divisas"

print(bienvenida)


dolares = 272.0
pesos_a_recibir = dolares * 21

billetes_200 = pesos_a_recibir // 200
billetes_100 = (pesos_a_recibir - (billetes_200 * 200)) // 100
billetes_50 = (pesos_a_recibir - (billetes_200 * 200) - (billetes_100 * 100)) // 50 
billetes_20 = (pesos_a_recibir - (billetes_200 * 200) - (billetes_100 * 100) \
               - (billetes_50 * 50)) // 20
monedas_10 = (pesos_a_recibir - (billetes_200 * 200) - (billetes_100 * 100) \
              - (billetes_50 * 50) - (billetes_20 * 20)) // 10
monedas_5 = (pesos_a_recibir - (billetes_200 * 200) - (billetes_100 * 100)  \
             - (billetes_50 * 50) - (billetes_20 * 20) - (monedas_10 * 10)) // 5
monedas_1 = (pesos_a_recibir - (billetes_200 * 200) - (billetes_100 * 100)  \
             - (billetes_50 * 50) - (billetes_20 * 20) - (monedas_10 * 10) - (monedas_5 * 5)) // 1


print(f'Cantidad en dolares {dolares}')
print(f'Total en pesos      {pesos_a_recibir}')

print(f'Billetes de 200 {billetes_200}')
print(f'Billetes de 100 {billetes_100}')
print(f'Billetes de 50  {billetes_50}')
print(f'Billetes de 20 {billetes_20}')
print(f'Monedasd de 10 {monedas_10}')
print(f'Monedasd de 5 {monedas_5}')
print(f'Monedasd de 1 {monedas_1}')

