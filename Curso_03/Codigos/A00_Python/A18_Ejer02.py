""" USO DEL IF

    evaluar un valor entre 0 y 100 y determinar el rango donde se encuentre
    0  - 10 en el rango de 0 a 10
    11 - 20 en el rango de 11 a 20
    21 - 30 en el rango de 21 a 30
    ....
    91 - 100 en el rango de 91 a 100
    
"""

valor = int(input("Proporcione un valor: "))

if valor >= 0 and valor <= 10:
    print("En el rango de 0 a 10")
elif valor > 10 and valor <= 20:
    print("En el rango de 11 a 20")
elif valor > 20 and valor <= 30:
    print("En el rango de 21 a 30")
elif valor > 30 and valor <= 40:
    print("En el rango de 31 a 40")
elif valor > 40 and valor <= 50:
    print("En el rango de 41 a 50")
elif valor > 50 and valor <= 60:
    print("En el rango de 51 a 60")
elif valor > 60 and valor <= 70:
    print("En el rango de 61 a 70")
elif valor > 70 and valor <= 80:
    print("En el rango de 71 a 80")
elif valor > 80 and valor <= 90:
    print("En el rango de 81 a 90")
elif valor > 90 and valor <= 100:
    print("En el rango de 91 a 100")
else:
    print("Valor fuera del rango")
