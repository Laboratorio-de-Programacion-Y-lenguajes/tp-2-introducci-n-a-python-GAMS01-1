# ============================================================
# MÓDULO 5: Loops
# ============================================================

def contar_hasta(n: int) -> list:
    """
    Retorna una lista con los números del 1 al n (inclusive).
    """
    # range(inicio, fin) genera números hasta fin-1, por eso usamos n+1
    return list(range(1, n + 1))


def tabla_multiplicar(n: int) -> list:
    """
    Retorna una lista con los primeros 10 múltiplos de n.
    """
    # Usamos una list comprehension para multiplicar n por cada número del 1 al 10
    return [n * i for i in range(1, 11)]


def suma_digitos(n: int) -> int:
    """
    Retorna la suma de los dígitos de un número entero positivo.
    """
    # Truco: convertimos el número a string para iterar por cada caracter/dígito
    return sum(int(digito) for digito in str(n))


def es_primo(n: int) -> bool:
    """
    Retorna True si n es un número primo.
    """
    if n < 2:
        return False
    # Verificamos si algún número entre 2 y la raíz de n lo divide exactamente
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci(n: int) -> list:
    """
    Retorna los primeros n números de la serie de Fibonacci.
    """
    if n <= 0: return []
    if n == 1: return [0]
    
    secuencia = [0, 1]
    # Mientras el tamaño de la lista sea menor a n, sumamos los dos últimos
    while len(secuencia) < n:
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia