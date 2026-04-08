### 1 - variables.py

**Herramienta**: Gemini (Asistente de Programación)

**Prompt usado**:
> Actuá como tutor de Python 3.13. Dame una receta paso a paso para:
> 1) pedir por consola nombre (str), edad (int) y ciudad (str),
> 2) validar que edad sea un entero,
> 3) devolver un string usando f-strings con el formato: "Soy {nombre}, tengo {edad} años y vivo en {ciudad}."
> No uses librerías externas. Mostrá una función `armar_mensaje(nombre, edad, ciudad)` con docstring.

**Resultado obtenido**:
La IA actuó como tutor y me guió paso a paso. Me explicó qué son los "f-strings" para formatear texto de manera moderna y me enseñó sobre "Type Hinting" (pistas de tipado) para definir claramente si una variable es un entero o un texto.

**¿Lo usaste tal cual o lo modificaste?**
Lo modifiqué de forma interactiva. El archivo real del repositorio tenía más funciones que el ejemplo básico del README. En lugar de pedir que me haga el trabajo, le pasé el código a la IA y le pedí que me explicara cómo encarar cada función. Así aprendí atajos útiles, como usar el atributo `type(valor).__name__` para extraer el tipo de dato, y a castear strings a decimales con `float()`.

---

### 2 - condicionales.py

**Herramienta**: Gemini (Asistente de Programación)

**Prompt usado**:
> Quiero implementar una función `clasificar_numero(n: int) -> str` en Python.
> Antes de escribir el código, haceme 3 preguntas para confirmar:
> - qué mensajes exactos debo devolver,
> - cómo tratar el 0,
> - y cómo priorizar condiciones.
> Después de mis respuestas, recién ahí proponé el código.

**Resultado obtenido**:
A través del patrón de interacción invertida, la IA me pidió analizar primero el código fuente real. En lugar de darme las respuestas de inmediato, me fue explicando conceptos lógicos clave. Por ejemplo, me enseñó por qué el orden de lectura de los `if` y `elif` de arriba hacia abajo es crítico (vital para el ejercicio de clasificar notas) y cómo funciona el operador módulo (`%`) para calcular los años bisiestos.

**¿Lo usaste tal cual o lo modificaste?**
Fui construyendo la solución basándome en las explicaciones del tutor. Usé la estructura lógica que armamos en conjunto, asegurándome de entender el "por qué" detrás de cada bloque lógico, lo que me permitió pasar las pruebas.

### 3 - listas.py

**Herramienta**: Gemini (Asistente de Programación)

**Prompt usado**:
> Actuá como un Senior Developer de Python. Explicame cómo resolver operaciones de listas (suma, filtrado, inversión y aplanamiento) usando las funciones nativas más eficientes de Python 3.13, priorizando el uso de List Comprehensions y evitando bucles 'for' tradicionales si es posible.

**Resultado obtenido**:
La IA me mostró cómo usar `sum()` para cálculos rápidos y cómo el "slicing" `[::-1]` permite invertir listas de forma elegante. También me explicó el concepto de List Comprehensions para filtrar pares y aplanar sublistas.

**¿Lo usaste tal cual o lo modificaste?**
Lo usé siguiendo las explicaciones. Me llamó la atención el truco de `dict.fromkeys()` para eliminar duplicados manteniendo el orden, algo que me pareció más limpio que crear una lista vacía y preguntar con un `if item not in...`.

### 4 - diccionarios.py

**Herramienta**: Gemini (Asistente de Programación)

**Prompt usado**:
> Explicame cómo funcionan los diccionarios en Python como si fuera un principiante. Necesito resolver funciones para contar palabras, invertir claves por valores y unir diccionarios. ¿Cuál es la forma más moderna de hacerlo en Python 3.13?

**Resultado obtenido**:
La IA me explicó la analogía de los casilleros (clave/valor). Me enseñó el método `.get()` para evitar errores al contar elementos y el operador `|` para combinar diccionarios de forma sencilla.

**¿Lo usaste tal cual o lo modificaste?**
Seguí la estructura recomendada. Me pareció muy útil la explicación de "Dictionary Comprehensions", ya que me permitió resolver la inversión de claves y valores en una sola línea de código, haciendo que el archivo sea mucho más fácil de leer.

### 5 - loops.py

**Herramienta**: Gemini (Asistente de Programación)

**Prompt usado**:
> Actuá como un mentor de algoritmos. Explicame cómo usar bucles for y while para resolver problemas clásicos como la serie de Fibonacci y la verificación de números primos. ¿Cómo puedo optimizar el cálculo de números primos en Python?

**Resultado obtenido**:
El mentor me explicó el uso de `range()` y cómo iterar sobre secuencias. Me enseñó un truco para sumar dígitos convirtiendo el número a string y me explicó por qué en el algoritmo de números primos solo es necesario iterar hasta la raíz cuadrada del número para ganar eficiencia.

**¿Lo usaste tal cual o lo modificaste?**
Seguí las recomendaciones lógicas. Para Fibonacci, opté por la solución con un bucle `while` que me resultó más intuitiva para controlar el tamaño exacto de la lista resultante, y apliqué la optimización de la raíz cuadrada en la función de números primos.

### 6 - funciones.py

**Herramienta**: Gemini (Asistente de Programación)

**Prompt usado**:
> Explicame el concepto de "Funciones de Orden Superior" en Python. Necesito implementar una composición de funciones, un decorador de memoización manual y una función de reducción sin usar librerías. ¿Cómo se usan las funciones como argumentos?

**Resultado obtenido**:
El asistente me enseñó que en Python las funciones son objetos. Me explicó cómo definir funciones dentro de otras funciones para lograr la composición y cómo usar diccionarios como "cache" para la memoización, evitando cálculos repetitivos.

**¿Lo usaste tal cual o lo modificaste?**
Lo usé tal cual. Fue muy útil entender el concepto de `*args` en la memoización para que la función acepte cualquier cantidad de parámetros, y la lógica de acumulación manual para la función `reducir`, lo que me ayudó a entender qué hace por detrás `functools.reduce`.

### 7 - operaciones.py

**Herramienta**: Gemini (Asistente de Programación)

**Prompt usado**:
> Explicame cómo manipular strings en Python para detectar palíndromos y contar vocales. Además, necesito implementar un Cifrado César. ¿Cómo puedo usar las funciones ord() y chr() para rotar letras sin romper caracteres especiales?

**Resultado obtenido**:
La IA me explicó el uso de `title()` para capitalizar y cómo limpiar strings con `split()`. Para el Cifrado César, me enseñó a usar aritmética modular (`% 26`) junto con los valores ASCII de las letras para que el desplazamiento sea circular.

**¿Lo usaste tal cual o lo modificaste?**
Seguí la lógica explicada. Para el palíndromo, usé la técnica de slicing `[::-1]` que aprendimos en el módulo de listas. En el Cifrado César, agregué una validación con `isalpha()` para asegurarme de que los espacios y puntos no se cifren.