""" LECTURA DE ARCHIVOS EXTERNOS CSV VERSIÓN MEJORADA

    Esta es la forma de leer un archivo CSV, defiiendo la ruta como un objeto
    
    Path.cwd() no te da la ubicación del archivo del programa, sino el 
    directorio desde el cual lo ejecutaste en la terminal.
    cwd significa Current Working Directory (Directorio de Trabajo Actual).

    ¿Por qué te ocurre esto?
    ------------------------
    Cuando ejecutas tu script desde la terminal o desde la terminal integrada 
    de un editor (como VS Code o PyCharm), es muy probable que te encuentres 
    parado en la carpeta InterSem/ al lanzar el comando.

    Por ejemplo, si en tu terminal hiciste algo como esto:
    
        # Estás parado aquí: /home/javier/Documentos/Programas/Python/InterSem
        python A01_Pandas/tu_programa.py

    Path.cwd() le pregunta al sistema: ¿En qué carpeta está parado el usuario 
    dentro de la terminal en este instante?, y la respuesta es .../InterSem/, 
    sin importar en qué subcarpeta viva el archivo .py que se está ejecutando.

    La Solución: Cómo obtener la ubicación exacta del archivo
    ---------------------------------------------------------
    Si lo que necesitas es obtener la carpeta exacta donde está guardado tu 
    archivo .py (sin importar desde dónde abras la terminal), debes usar la 
    variable especial __file__.

    ¿Qué hace este cambio?
    ----------------------
    __file__: Le da a Python la ruta absoluta de tu archivo script actual.
    .resolve(): Limpia la ruta para asegurarse de que sea completa e inequívoca.
    .parent: Accede a la carpeta contenedora directamente superior, que en este
    caso será /home/javier/Documentos/Programas/Python/InterSem/A01_Pandas

    Tip práctico: 
    -------------
    Si vas a leer o guardar archivos de Excel/CSV en esa misma carpeta usando 
    pandas, siempre es recomendable construir las rutas partiendo de 
    
        Path(__file__).resolve().parent 
        
    para evitar que el código falle cuando lo ejecutes desde otras terminales.
"""

import pandas as pd 
from pathlib import Path

# Obtiene la ruta exacta de este archivo .py y luego extrae su carpeta contenedora (.parent)
ruta_del_script = Path(__file__).resolve().parent
ruta_del_script = ruta_del_script / 'ArchivosExternos/Precipitaciones.csv'
print(ruta_del_script)

ruta1 = Path(__file__)
ruta2 = Path(__file__).resolve()
ruta3 = Path(__file__).resolve().parent
print('ruta 1:', ruta1)
print('ruta 2:', ruta2)
print('ruta 3:', ruta3)


df = pd.read_csv(ruta_del_script)

print(df)
