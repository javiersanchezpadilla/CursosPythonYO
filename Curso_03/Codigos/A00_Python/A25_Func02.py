""" PARÁMETROS Y ARGUMENTOS

    Los parámetros son las variables que declaras en la definición de la 
    función para recibir datos de entrada. Los argumentos son los valores 
    reales que le pasas a la función cuando la llamas.
"""

        # 'nombre' y 'ciudad' son PARÁMETROS
def dar_bienvenida(nombre, ciudad):
    print(f"Hola {nombre}, qué gusto verte desde {ciudad}.")

# "Javier" y "Acapulco" son ARGUMENTOS
dar_bienvenida("Javier", "Acapulco")
