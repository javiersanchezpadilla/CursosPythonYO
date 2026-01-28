# EN ESTAS FUNCIONES SOLO IMPRIMOS VALORES

def saludo():
    print('Hola')

def mi_saludo(nombre):
    print(f'Hola {nombre}')


saludo()            # llamamos a la funcion
#mi_saludo()         # Llamo a la funcion con error
mi_saludo('Javier')

# SI QUEREMOS QUE NUESTRAS FUNCIONES RETORNEN UN VALOR PARA MANIPULAR

def sumar(a, b):
    resultado = a + b
    return resultado


valor = sumar(10, 20)
print(valor)
print(sumar(1, 1))

# definir una funcion que pida un valor e imprima una lista de valores desde el 1 al valor
def pide_valor():
    valor = int(input('Proporcione un valor final '))
    for cont in range(0, valor+1):
        print(cont)

pide_valor()

print('----------------------')
def imprimir_pares_hasta(n):
    for numero in range(1, n):
        if numero % 2 == 0:
            print(numero)


imprimir_pares_hasta(9)