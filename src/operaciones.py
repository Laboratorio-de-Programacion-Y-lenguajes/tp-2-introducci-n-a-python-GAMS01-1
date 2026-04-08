# ============================================================
# MÓDULO 7: Operaciones con Strings
# ============================================================

def es_palindromo(texto: str) -> bool:
    """
    Retorna True si el texto es palíndromo (ignorando espacios y mayúsculas).
    """
    # Limpiamos el texto: a minúsculas y sacamos espacios
    limpio = "".join(texto.lower().split())
    # Comparamos con su versión invertida usando slicing [::-1]
    return limpio == limpio[::-1]


def capitalizar_palabras(texto: str) -> str:
    """
    Capitaliza la primera letra de cada palabra.
    """
    # title() es el método perfecto para esto
    return texto.title()


def contar_vocales(texto: str) -> int:
    """
    Retorna la cantidad de vocales (a,e,i,o,u) en el texto.
    """
    vocales = "aeiou"
    # Sumamos 1 por cada caracter que esté en nuestro string de vocales
    return sum(1 for char in texto.lower() if char in vocales)


def caesar_cipher(texto: str, desplazamiento: int) -> str:
    """
    Aplica el cifrado César al texto con el desplazamiento dado.
    """
    resultado = ""
    for char in texto:
        if char.isalpha(): # Solo procesamos letras
            # Determinamos si es 'a' o 'A' para el punto de partida (ASCII)
            start = ord('a') if char.islower() else ord('A')
            # Aplicamos la fórmula matemática del desplazamiento (módulo 26)
            nuevo_char = chr(start + (ord(char) - start + desplazamiento) % 26)
            resultado += nuevo_char
        else:
            resultado += char
    return resultado