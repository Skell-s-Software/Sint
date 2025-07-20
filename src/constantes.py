# Modulo con lista de funciones a transpilar

funciones = {
    # Funciones de entrada/salida
    "Salida(": "terminal.print(f",
    "Entrada(": "input(",
    # Funciones de control de flujo
    "Si(": "if ",
    "SiNoEntonces(": "elif",
    "SiNo(": "else:",
    # Funciones de iteración
    "Repetir(": "for ",
    "Mientras(": "while ",
    # Funciones de manejo de excepciones
    "Intentar(": "try:",
    "Excepcion(": "except",
    "Finalmente(": "finally:",
    # Funciones de definición
    "Metodo(": "def ",
    "Clase(": "class ",
    # Funciones de importación
    "DesdeLibreria:": "from",
    "ImportarFuncion:": "import",
    "ConApodo:": "as",
    # Manejo de final de metodo
    "):": ":",
    # Funciones de utilidades
    "DentroDe:": "in",
    "Rango(": "range(",
    "Largo(": "len(",
    "HacerCon(": "with ",
    # Tipos de datos
    "Lista(": "list(",
    "Diccionario(": "dict(",
    "Conjunto(": "set(",
    "Tupla(": "tuple(",
    "Booleano(": "bool(",
    "Entero(": "int(",
    "Decimal(": "float(",
    "Cadena(": "str(",
    "Ninguno": "None",
    "Verdadero": "True",
    "Falso": "False",
    }
