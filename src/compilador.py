# Modulo de conversión

# Importacion de modulos
from explorador import leer_fichero
from constantes import funciones
from rich.console import Console
import subprocess

terminal = Console()

def transpilar(codigo: str):
    codigoPy = codigo[0]
    for buscar, remplazar in funciones.items():
        codigoPy = codigoPy.replace(buscar, remplazar)
    print(f"Codigo Transpilado:\n{codigoPy}")
    if codigo[1] == "streamlit":
        codigoPy = "from rich.console import Console\nterminal = Console()\n" + codigoPy
        with open("index.py", "w", encoding="utf-8") as archivo:
            archivo.write(codigoPy)
        try:
            subprocess.run("streamlit run index.py", shell=True)
        except KeyboardInterrupt:
            print("Streamlit detenido por el usuario.")
    else:
        return codigoPy

def ejecucion(codigo: str):
    try:
        # Importamos la terminal para evitar errores
        contexto = {
            "terminal": terminal
        }
        exec(f"""{codigo}""", contexto)
    except Exception as e:
        print(e)

codigoSint = leer_fichero()

codigoPy = transpilar(codigoSint)

ejecucion(codigoPy)

