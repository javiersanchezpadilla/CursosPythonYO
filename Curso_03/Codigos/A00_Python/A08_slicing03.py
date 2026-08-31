# 4. El Truco del Paso Negativo (Invertir Cadenas)
# --------------------------------------------------
# Si colocas un paso negativo como -1, Python recorre la cadena de derecha a 
# izquierda:
palabra = "Acapulco"

# Invierte el texto por completo
palabra_invertida = palabra[::-1]

print(palabra_invertida) # Salida: 'oclupacA'
