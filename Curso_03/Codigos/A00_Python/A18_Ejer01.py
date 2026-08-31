""" USO DEL IF

    evaluar un valor entre 0 y 100 y determinar el rango donde se encuentre
    0  - 10 en el rango de 0 a 10
    11 - 20 en el rango de 11 a 20
    21 - 30 en el rango de 21 a 30
    ....
    91 - 100 en el rango de 91 a 100
    
"""

valor = 10

if valor >= 0 and valor <= 10:
    print("En el rango de 0 a 10")

if valor > 10 and valor <= 20:
    print("En el rango de 11 a 20")

if valor > 20 and valor <= 30:
    print("En el rango de 21 a 30")
    
# ....

if valor > 90 and valor <= 100:
    print("En el rango de 91 a 100")

