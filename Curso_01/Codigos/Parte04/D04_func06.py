mi_lista = list(range(1,10))

def cuadrado(n):
    return n ** 2

def calcular_lista(lista_de_numeros):
    for numero in lista_de_numeros:
        resultado = cuadrado(numero)
        print(f'El cuadrado de {numero} es {resultado}')


calcular_lista(mi_lista)