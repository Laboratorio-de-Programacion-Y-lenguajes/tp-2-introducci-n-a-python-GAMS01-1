# ============================================================
# MÓDULO 6: Funciones
# ============================================================

def aplicar_funcion(lista: list, func) -> list:
    """
    Aplica func a cada elemento de la lista y retorna la nueva lista.
    """
    # Usamos una list comprehension para pasar cada x por la función 'func'
    return [func(x) for x in lista]


def componer(f, g):
    """
    Retorna una nueva función que aplica g y luego f.
    """
    # Definimos una función interna que recibe el valor y la devolvemos
    def funcion_compuesta(x):
        return f(g(x))
    return funcion_compuesta


def memoizar(func):
    """
    Retorna una versión de func que cachea sus resultados.
    """
    cache = {}
    def version_con_cache(*args):
        # Si el argumento ya está en el diccionario, lo devolvemos sin calcular
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return version_con_cache


def reducir(lista: list, func, inicial):
    """
    Aplica func acumulativamente a los elementos de lista,
    comenzando con inicial. NO uses functools.reduce
    """
    resultado = inicial
    for elemento in lista:
        # El resultado actual se combina con el siguiente elemento usando 'func'
        resultado = func(resultado, elemento)
    return resultado
