""" solicitar la edad de una perosna, si edad < 18 años imprimir que es 
    menor de edad, en otro caso es menor de edad"""
    
edad = int(input("Edad: "))

if edad < 18:
    print("Menor de edad")
else:
    print("Mayor de edad")
    

print("\nVERSION DOS DEL IF")
print("Mayor de edad" if edad >= 18 else "Menor de edad")
