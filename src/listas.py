# ============================================================
# MÓDULO 3: Listas
# ============================================================

def suma_lista(numeros: list) -> int | float:
    """
    Retorna la suma de todos los elementos de la lista.
    """
    # Python tiene una función incorporada llamada sum() que es súper eficiente.
    return sum(numeros)


def filtrar_pares(numeros: list) -> list:
    """
    Retorna una nueva lista con solo los números pares.
    """
    # Usamos una "List Comprehension" (es un atajo muy potente de Python).
    # Se lee: "Poné la n en la lista SI el resto de n / 2 es cero".
    return [n for n in numeros if n % 2 == 0]


def invertir_lista(lista: list) -> list:
    """
    Retorna la lista invertida SIN modificar la original.
    """
    # El truco [::-1] crea una copia de la lista pero recorriéndola de atrás hacia adelante.
    return lista[::-1]


def eliminar_duplicados(lista: list) -> list:
    """
    Retorna una nueva lista sin elementos duplicados,
    manteniendo el orden de primera aparición.
    """
    # No podemos usar set() simplemente porque set() pierde el orden original.
    # Usamos dict.fromkeys() que elimina duplicados pero respeta el orden.
    return list(dict.fromkeys(lista))


def aplanar_lista(lista: list) -> list:
    """
    Dada una lista de listas, retorna todos los elementos en una sola lista.
    Ejemplo: aplanar_lista([[1,2],[3,4]]) -> [1, 2, 3, 4]
    """
    # Usamos un bucle doble dentro de una lista: 
    # "Para cada sublista, agarrá cada item y ponelo en la lista principal".
    return [item for sublista in lista for item in sublista]