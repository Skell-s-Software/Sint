# Modulo de extracción de Archivo mediante argumentos/parametros

# Importaciom de sys para obtemer parametros
import sys

# Prueba de viabilidad de sys
# print(f"archivo: {sys.argv[1]}")

# Lógica de argumentos:
def argumentos():
    if len(sys.argv) > 1:
        return sys.argv
    else:
        return "No se encontraron argumentos"
