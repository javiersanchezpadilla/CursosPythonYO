"""
Dada una tupla llamada info_ciudades que contiene tres tuplas dentro. 
Cada tupla interna representa una ciudad y contiene el nombre de la ciudad, 
la población y el país.
("Buenos Aires", 3000000, "Argentina"), ("Madrid", 3200000, "España"), 
("Tokio", 13929286, "Japón").
Imprime un mensaje para cada ciudad siguiendo el formato siguiente:
"La ciudad de [nombre de la ciudad] en [país] tiene una población de 
[población] habitantes"
Utiliza los indices requeridos para acceder a los datos especificos de 
cada pais, crea las variables que consideres necesarias y con el empleo de 
cadenas literales imprime tres mensajes en el orden siguiente:
"La ciudad de Buenos Aires en Argentina tiene una población de 3000000 habitantes"
"La ciudad de Madrid en España tiene una población de 3200000 habitantes"
"La ciudad de Tokio en Japón tiene una población de 13929286 habitantes"
"""

info_ciudades = (("Buenos Aires", 3000000, "Argentina"), ("Madrid", 3200000, "España"), 
                 ("Tokio", 13929286, "Japón"))
ciudad1, ciudad2, ciudad3 = info_ciudades

print(f'La ciudad de {ciudad1[0]} en {ciudad1[2]} tiene una población de {ciudad1[1]} habitantes')
print(f'La ciudad de {ciudad2[0]} en {ciudad2[2]} tiene una población de {ciudad2[1]} habitantes')
print(f'La ciudad de {ciudad3[0]} en {ciudad3[2]} tiene una población de {ciudad3[1]} habitantes')
