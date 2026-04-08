# ============================================================
# MÓDULO 4: Diccionarios
# ============================================================

def contar_palabras(texto: str) -> dict:
    """
    Retorna un diccionario con la frecuencia de cada palabra.
    """
    palabras = texto.lower().split()
    frecuencia = {}
    for p in palabras:
        # get(p, 0) intenta buscar la palabra; si no existe, devuelve 0. 
        # Luego le sumamos 1. ¡Es más limpio que usar un if!
        frecuencia[p] = frecuencia.get(p, 0) + 1
    return frecuencia


def invertir_diccionario(d: dict) -> dict:
    """
    Retorna un nuevo diccionario con claves y valores intercambiados.
    """
    # Usamos un "Dictionary Comprehension" (igual que con las listas, pero con llaves).
    return {valor: clave for clave, valor in d.items()}


def merge_diccionarios(d1: dict, d2: dict) -> dict:
    """
    Combina dos diccionarios. Si hay claves repetidas, prevalece d2.
    """
    # El operador | (pipe) es la forma más moderna (Python 3.9+) de unir diccionarios.
    return d1 | d2


def filtrar_por_valor(d: dict, minimo: int) -> dict:
    """
    Retorna un nuevo diccionario con solo los pares cuyo valor sea >= minimo.
    """
    # Filtramos usando ítems (clave y valor) y reconstruimos el diccionario.
    return {k: v for k, v in d.items() if v >= minimo}
