# Modulo de extracción de Archivo mediante argumentos/parametros

# Importaciom de sys para obtemer parametros
import sys

# Prueba de viabilidad de sys
# for arg in sys.argv:
#     print(f"Argumento: {arg}")

# Lógica de argumentos:
def argumentos():
    if len(sys.argv) == 1:
        return "No se proporcionaron argumentos"
    elif len(sys.argv) == 2:
        return (sys.argv[1], False)  # Retorna el nombre del archivo
    elif len(sys.argv) == 3 and sys.argv[2] == "streamlit":
        return (sys.argv[1], sys.argv[2])  # Retorna el nombre del archivo y el segundo argumento
    else:
        return f"Argumento invalido: {sys.argv[2]}"
