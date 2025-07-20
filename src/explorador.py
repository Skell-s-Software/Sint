# Modulo que extrae el contenido del fichero

# Importación de librerías y módulos
from extractor import argumentos
import re

def leer_fichero():
# Obtener argumentos
    arg = argumentos()

# Busqueda del archivo en directorio
    with open(arg[0], 'r', encoding='utf-8') as fichero:
        codigo = fichero.read()
        return (codigo, arg[1])