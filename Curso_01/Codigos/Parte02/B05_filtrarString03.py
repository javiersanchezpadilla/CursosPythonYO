"""
    Escribe un programa en el que declares una variable llamada frase 
    y le asignes el texto que prefieras. Debes cumplir con las siguientes 
    condiciones:
    La frase debe contar un espacio al inicio y otro al final, por ejemplo 
    " Python es genial ".
    La frase debe tener todas sus palabras separadas por un único espacio.
    Crea una variable llamada palabras_en_frase donde  almacenes el número 
    de palabras contenidas en la frase. Utiliza los métodos correspondientes 
    para  conseguir las siguientes acciones en el orden que se describen a 
    continuación:
    Eliminar los espacios al incio y al final de la frase.
    Contar el número de palabras contenidas en la frase.
    Finalmente, muestra el resultado en pantalla.
"""
frase = " Python es genial "
palabras_en_frase = frase.strip().count(" ") + 1
print(palabras_en_frase)