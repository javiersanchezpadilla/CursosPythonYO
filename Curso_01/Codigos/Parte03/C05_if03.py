"""
Desarrolla un programa que defina dos variables, usuario  y  
contraseña. Luego, escribe una estructura de control que verifique 
si el usuario es igual a "admin" y si la contraseña es igual a "abc123". 
Si ambas condiciones se cumplen, imprime "Acceso concedido"
Utiliza el operador matemático de doble igualdad (==) para preguntar con 
un IF si se cumple determinada condición. Por ejempo: if usuario == "admin"
"""
usuario = input('Introduzca el usuario: ')
contraseña =  input('Introduzca la contraseña: ')
if usuario == 'admin' and contraseña == 'abc123':
    print('Acceso concedido')
