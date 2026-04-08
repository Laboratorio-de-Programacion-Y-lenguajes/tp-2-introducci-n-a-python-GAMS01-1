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