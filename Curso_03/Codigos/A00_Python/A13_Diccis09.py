# los diccionarios se componen de un par que es una clave y un valor
# Las claves son unicas (no se pueden repetir)

dic = {}
print(type(dic))

edades = {'juan': 20, 'carlos':40, 'Maria':16}

#print(edades[1])       No puedo indexar no son secuencias ordenadas
print(edades['carlos'])

edades['jose'] = 30     # Agregmos un elemento al diccionario
print(edades)

edades['Maria'] = 27    # modificamos un valor
print(edades)

# metodos de los diccionarios
print(edades.keys())        # obtiene solo las llaves
print(edades.values())      # obtiene solo los valores
print(edades.items())       # items convierte en tupla de listas
print(edades.get('juan'))   # obtiene no por indice
edades.update({'carlos': 15})
print(edades)