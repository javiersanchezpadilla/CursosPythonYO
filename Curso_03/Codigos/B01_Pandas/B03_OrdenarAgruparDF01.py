"""  AGRUPAR DATOS EN PANDAS

    Agrupar datos en Pandas es una de las tareas más comunes e importantes 
    en el análisis de datos. Para esto se utiliza el método .groupby().
    La forma más sencilla de entender .groupby() es pensar en el proceso 
    Dividir - Aplicar - Combinar (Split-Apply-Combine):

    A)  Dividir (Split): Separa las filas del DataFrame en grupos (ejemplo, 
        por 'Categoría' o 'Ciudad').
    B)  Aplicar (Apply): Ejecuta una operación matemática o función a cada 
        grupo por separado (promedio, suma, conteo, etc.).
    C)  Combinar (Combine): Une todos los resultados en un nuevo DataFrame o 
        tabla resumida.

    Un Ejemplo Práctico Paso a Paso
    -------------------------------
    Imagina que tenemos un registro de ventas de una tienda con diferentes 
    sucursales y productos:

"""
import pandas as pd

# Creamos nuestro DataFrame de ejemplo
datos = {
    "Sucursal": ["Norte", "Norte", "Sur", "Sur", "Norte", "Sur"],
    "Producto": ["Manzanas", "Pan", "Manzanas", "Pan", "Leche", "Leche"],
    "Unidades": [10, 5, 12, 8, 15, 20],
    "Venta_Total": [100, 25, 120, 40, 150, 200]
}

df = pd.DataFrame(datos)
print(df)

# OPERACIONES BÁSICAS (SUMA, PROMEDIO, CONTEO)
# Si queremos saber cuánto vendió cada sucursal en total, agrupamos por la 
# columna "Sucursal" y aplicamos .sum():
# Suma total por Sucursal
print("\nVentas por sucursal")
ventas_por_sucursal = df.groupby("Sucursal")["Venta_Total"].sum()
print(ventas_por_sucursal)

# saber el promedio de unidades vendidas por producto:
# Promedio de unidades por Producto
promedio_unidades = df.groupby("Producto")["Unidades"].mean()
print(promedio_unidades)

# Agrupar por Múltiples Columnas
# Podemos crear subdivisiones pasando una lista de columnas. Por ejemplo, 
# para saber las ventas agrupadas por Sucursal y luego por Producto:
# Agrupamos por dos columnas a la vez
print("\nVentas por sucursal y producto")
ventas_detalle = df.groupby(["Sucursal", "Producto"])["Venta_Total"].sum()
print(ventas_detalle)

# Aplicar Múltiples Operaciones con .agg()
# ¿Qué pasa si en una sola consulta quieres saber el promedio de unidades y la 
# suma total de dinero de cada sucursal? Usamos el método .agg() pasándole un 
# diccionario con las instrucciones: 
# Múltiples operaciones específicas por columna
print("\nMultiples operaciones AGG AGGREGATE")
resumen = df.groupby("Sucursal").agg({
    "Unidades": "mean",             # Calcula el promedio de unidades
    "Venta_Total": ["sum", "max"]   # Calcula suma y el valor máximo de venta
})

print(resumen)

# Tip Clave: .reset_index()
# Cuando usas .groupby(), la columna por la que agrupaste (como 'Sucursal') se 
# convierte en el índice de la tabla resultado. Si prefieres mantenerla como 
# una columna normal para seguir trabajando con ella fácilmente, 
# usa .reset_index() al final:
# Convierte el resultado de nuevo en un DataFrame limpio
print("\nReseteando el índice para que sea el original")
df_limpio = df.groupby("Sucursal")["Venta_Total"].sum().reset_index()
print(df_limpio)


# Contar la suma total de piezas de artículos (.sum())
# Si la columna Unidades indica la cantidad de artículos que se llevó el 
# cliente en cada venta, se debe agrupar por Sucursal y aplicar el método .sum()
# Sumamos las Unidades para saber el total de artículos físicos vendidos
print("\nUnidades vendidas por unidad")
total_articulos = df.groupby("Sucursal")["Unidades"].sum().reset_index()
print(total_articulos)

# Contar cuántas ventas o transacciones se hicieron .count()
# Si lo que deseas es saber cuántas operaciones/tickets de venta se 
# registraron por sucursal (sin importar la cantidad de productos por ticket), 
# usas el método .count() o .value_counts():
# mediante groupby() y .count()
# Cuenta cuántas filas (ventas) hay registradas por sucursal
print("\nTotal de ventas registradas por tienda (usando groupby y count)")
total_ventas_registradas = df.groupby("Sucursal")["Producto"].count().reset_index()
print(total_ventas_registradas)

# De forma ultra rápida con .value_counts()
# Si solo se requiere un conteo directo de las filas de una columna sin usar 
# groupby, se puedes hacer
print("\nTotal de ventas registradas por tienda (usando value_count")
print(df["Sucursal"].value_counts())
