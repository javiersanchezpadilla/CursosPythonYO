""" El método resolve() del módulo pathlib sirve para convertir cualquier ruta 
    (relativa o simbólica) en su ruta absoluta real y canónica, resolviendo en 
    el proceso todos los enlaces simbólicos (symlinks) y las referencias 
    especiales de navegación como . (directorio actual) y .. (directorio 
    padre).

    ¿Para qué nos sirve en la práctica?
    -----------------------------------
    1. Eliminar la ambigüedad de rutas relativas
    --------------------------------------------
    Si estás trabajando con una ruta relativa (como './datos/archivo.csv'), su 
    significado depende de la carpeta desde donde ejecutes el script. Al aplicar 
    .resolve(), Pandas o tu programa obtienen la ruta absoluta completa desde 
    la raíz del sistema de archivos.
"""
from pathlib import Path

# Ruta relativa simple
ruta_relativa = Path("datos/mi_archivo.csv")

# Convertir a ruta absoluta canónica
ruta_absoluta = ruta_relativa.resolve()

print(ruta_relativa) 
# Salida: datos/mi_archivo.csv

print(ruta_absoluta) 
# Salida: /home/javier/Documentos/Programas/Python/InterSem/A01_Pandas/datos/mi_archivo.csv
