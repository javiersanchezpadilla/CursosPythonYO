"""
    Escribe un programa en Python que haga lo siguiente: 
    1. Crea dos variables string1 y string2 luego almacena en ellas 
       las palabras: "aprender" y "python". Respectivamente.
    2. Concatena ambos strings para formar la frase "Aprender Python" 
       y almacena el resultado en una nueva variable resultado
    3. Aplica un método para convertir solo la primera letra de cada 
       palabra en mayúscula. Imprime el resultado final. Deberá quedar 
       de la siguiente forma: Aprender Python
    4. Imprime el resultado final.
"""

string1 = 'aprender'
string2 = 'python'
resultado = string1 + " " + string2
print(string1.capitalize() + " " + string2.capitalize())

