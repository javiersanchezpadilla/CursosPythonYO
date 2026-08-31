# Casos de Uso Reales en Proyectos
# --------------------------------
# Extraer elementos de fechas formateadas
fecha = "17/08/2026"  # Formato DD/MM/YYYY

dia = fecha[:2]       # '17'
mes = fecha[3:5]      # '08'
anio = fecha[6:]      # '2026'

print(f"Año: {anio}, Mes: {mes}, Día: {dia}")


# Ocultar datos sensibles (enmascaramiento)
# -----------------------------------------

tarjeta = "1234567890123456"

# Muestra solo los últimos 4 dígitos
ultimos_digitos = tarjeta[-4:]
enmascarado = "*" * 12 + ultimos_digitos

print(enmascarado) # Salida: ************3456
