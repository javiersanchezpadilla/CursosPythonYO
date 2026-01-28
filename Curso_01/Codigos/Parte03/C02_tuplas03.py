"""
Dada la tupla datos_personales que contiene los siguientes elementos: 
("Maria", "Perez", 35, "Ingeniera"), utiliza la segmentación de tuplas 
para imprimir únicamente el nombre y la profesión de María en un mensaje 
que diga: "Maria es Ingeniera".
Para esto puedes crear variables que contengan el nombre y la profesion de 
Maria según el indice en el que se encuentra en la variable datos_personales   
Recuerda emplear cadenas lietarles para imprimir el mensaje esperado: "Maria es Ingeniera"
"""

datos_personales = ("Maria", "Perez", 35, "Ingeniera")
nombre = datos_personales[0]
profesion = datos_personales[3]
print('{} es {}'.format(nombre, profesion))