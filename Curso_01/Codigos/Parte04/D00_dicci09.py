# # Creando un diccionario para guardar datos de contacto
# contactos = { "Juan": "555-1234", "Ana": "222-5678", "Pedro": "333-9012"}

# del contactos["Pedro"] o contactos.pop('Pedro')


# # Accediendo a un valor
# print("El teléfono de Juan es:", contactos["Juan"])

# # Agregando un nuevo contacto
# contactos["María"] = "444-3456"

# # Modificando un valor existente
# contactos["Ana"] = "222-8765"

# # Eliminando un contacto
# del contactos["Pedro"]
# contactos.pop('Pedro')

# # Imprimiendo todos los contactos
# for nombre, telefono in contactos.items():
#     print(nombre, ":", telefono)

estudiantes = {
    "Juan": [20, ["Matemáticas", "Física", "Historia"]],
    "Ana": [22, ["Biología", "Química", "Literatura"]],
    "Pedro": [19, ["Programación", "Bases de Datos", "Redes"]]
}

for nombre, lista_valores in estudiantes.items():
    print(nombre)
    print(lista_valores)


    # print(f'{nombre} tiene los siguientes datos')
    # for edad, lista_materias in lista_valores:
    #     print(f'Edad {edad}')
    #     for materia in lista_materias:
    #         print(f'{materia}')
