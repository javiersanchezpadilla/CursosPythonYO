""" OPERACIONES BASICAS DE CONJUNTOS
"""
colores = {"rojo", "verde"}

# AGREGAR ELEMENTOS
# Agrega un elemento al conjunto
colores.add("azul")

# Agrega múltiples elementos de una lista/set
colores.update(["amarillo", "blanco"])  

print(colores)  # {'rojo', 'verde', 'azul', 'amarillo', 'blanco'}

# ELIMINAR ELEMENTOS
# Elimina 'rojo'. Si NO existe, lanza un KeyError.
colores.remove("rojo")     

# Intenta eliminar 'negro'. Si NO existe, NO da error.
colores.discard("negro")   

# Vaciar todo el conjunto
# colores.clear()