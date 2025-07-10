# Modulo de conversión

# Importacion de modulos
from explorador import leer_fichero
from constantes import funciones

def transpilar(codigo: str):
    codigoPy = codigo
    for buscar, remplazar in funciones.items():
        codigoPy = codigoPy.replace(buscar, remplazar)
    return codigoPy

def ejecucion(codigo: str):
    try:
        exec(f"""{codigo}""")
    except Exception as e:
        print(e)

codigoSint = leer_fichero()

codigoPy = transpilar(codigoSint)

ejecucion(codigoPy)

