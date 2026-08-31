""" OPERACIONES MATEMÁTICAS DE CONJUNTOS

    Aquí es donde los conjuntos demuestran toda su potencia. Python permite 
    realizar operaciones de lógica de conjuntos de forma extremadamente 
    legible, ya sea con métodos o con operadores de símbolos:

    Imaginemos dos grupos de estudiantes inscritos en materias:
"""
programacion = {"Javier", "Ana", "Carlos", "Sofia"}
matematicas = {"Carlos", "Sofia", "Luis", "Elena"}

# UNION (conj_a | conj_b  o  conj_a.union(conj_b))
# ¿Quiénes están inscritos en AL MENOS una de las dos materias?
# todos = programacion | matematicas
todos = programacion.union(matematicas)

print('Union', todos)       # {'Javier', 'Ana', 'Carlos', 'Sofia', 'Luis', 'Elena'}

# INTERSECCION  (conj_a & conj_b   o   conj_a.intersection(conj_b))
# ¿Quiénes están inscritos en AMBAS materias?
# ambas = programacion & matematicas
ambas = programacion.intersection(matematicas)

print('Intersección', ambas)    # {'Carlos', 'Sofia'}

# DIFERECIA (conj_a - conj_b    o   conj_a.difference(conj_b))
# Devuelve los elementos que están en el primer conjunto pero NO en el segundo.
# ¿Quiénes están SOLO en programación (y no en matemáticas)?
# solo_programacion = programacion - matematicas
solo_programacion = programacion.difference(matematicas)

print('Diferencia', solo_programacion)    # {'Javier', 'Ana'}

# DIFERENCIA SIMÉTRICA (conj_a ^ conj_b   o   conj_a.symmetric_difference(conk_b))
# Devuelve los elementos que están en uno u otro conjunto, pero NO en ambos 
# (excluye la intersección).
# ¿Quiénes están en solo una materia (no en las dos)?
# exclusivos = programacion ^ matematicas
exclusivos = programacion.symmetric_difference(matematicas)

print(exclusivos)           # {'Javier', 'Ana', 'Luis', 'Elena'}