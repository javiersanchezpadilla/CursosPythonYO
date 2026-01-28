"""Este programa permite determinar con base a una lista si todos los 
    valores contenidos son positivos como resultado revuelve un valor 
    verdadero o falso"""
listanumeros = [1,2,3,4  ,5,   1,-10]
def todos_positivos    (parametroLista):
    resultado=True
    for n in parametroLista:
        if n<0:
            resultado=False
    return resultado
print(todos_positivos(listanumeros))