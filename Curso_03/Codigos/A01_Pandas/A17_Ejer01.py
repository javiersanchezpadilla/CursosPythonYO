""" Agregación de Series en Pandas 3

    Considera una serie de Pandas que representa las ventas de un mes, donde 
    cada valor corresponde a las ventas de un día específico. No modifiques 
    la serie de Pandas brindada en el ejercicio.
    Realiza las siguientes operaciones y muestra los resultados empleando los 
    métodos correspondientes:

    Calcula el total de ventas del mes. Almacena su valor en una variable 
    llamada: total_ventas_mes
    Encuentra el día con las ventas más bajas. Almacena su valor en una variable 
    llamada: dia_ventas_mas_bajas
    Determina el promedio mensual de ventas. Almacena su valor en una variable 
    llamada: promedio_ventas_mes
"""
import pandas as pd

# Serie de ventas del mes
ventas_mes = pd.Series([220, 235, 260, 213, 202, 298, 265, 198, 220, 230, 190, 215, 275, 222, 218, 245, 233, 210, 290, 210,
                        215, 220, 225, 230, 245, 250, 260, 270, 280, 295])
                        
total_ventas_mes = ventas_mes.sum()
dia_ventas_mas_bajas = ventas_mes.min()
promedio_ventas_mes = ventas_mes.mean()

print('Total ventas del mes', total_ventas_mes)
print('Venta mas baja del mes', dia_ventas_mas_bajas)
print('Promedio de ventas del mes', promedio_ventas_mes)
