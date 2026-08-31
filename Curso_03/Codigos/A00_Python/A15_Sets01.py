""" MANEJO DE CONJUNTOS

"""
# 1. Usando llaves {}
frutas = {"manzana", "plátano", "naranja"}

# 2. Convertir otra colección usando set()
numeros_lista = [1, 2, 2, 3, 4, 4, 4, 5]
numeros_unicos = set(numeros_lista)

print(numeros_unicos)
# Salida: {1, 2, 3, 4, 5}  <-- Elimina los duplicados automáticamente

#CUIDADO CON EL CONJUNTO VACÍO
# Esto crea un DICCIONARIO vacío, no un set
vacio_error = {}      

# Esta es la forma correcta de crear un set vacío.
vacio_correcto = set() 
