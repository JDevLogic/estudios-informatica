# === Extender Tipos de Datos Nativos en Python ===
#
# Python nos permite crear nuestras propias clases que "heredan" de los tipos de datos
# que ya vienen incorporados en el lenguaje, como `list`, `dict`, `str`, etc.
# Esto es útil cuando queremos añadir funcionalidades específicas a estos tipos
# sin perder todas las características que ya tienen.

# --- Creación de una Clase que Extiende `list` ---

# Aquí, creamos una nueva clase llamada `Lista`.
# Al poner `(list)` después del nombre de la clase, le estamos diciendo a Python
# que nuestra clase `Lista` va a ser una "hija" de la clase `list`.
# Esto significa que nuestra clase `Lista` heredará automáticamente TODOS
# los métodos y comportamientos de una lista normal (append, pop, sort, etc.).
class Lista(list):
    """
    Esta es nuestra versión personalizada de una lista.
    Hereda todas las funcionalidades de `list` y añade métodos nuevos.
    """

    # --- Añadiendo un Nuevo Método ---
    # Ahora, podemos definir nuestros propios métodos para añadir funcionalidades.
    # En este caso, creamos un método llamado `prepend`.
    def prepend(self, item):
        """
        Añade un elemento al PRINCIPIO de la lista.
        Las listas normales no tienen un método `prepend`, solo `append` (que añade al final).

        Args:
            item: El elemento que se va a añadir a la lista.
        """
        # `self` aquí se refiere a la propia instancia de la lista.
        # Usamos el método `insert(0, item)`, que ya existe en todas las listas,
        # para insertar el `item` en la posición 0 (el principio).
        self.insert(0, item)

# --- Demostración del Funcionamiento ---

# 1. Creamos una instancia de nuestra nueva clase `Lista`.
#    Le pasamos una lista normal `[1, 2, 3]` para inicializarla.
lista = Lista([1, 2, 3])

# 2. Podemos usar los métodos que ya existían en las listas normales.
#    Por ejemplo, `append` funciona exactamente igual porque lo hemos heredado.
lista.append(4)
print(f"Después de usar append(4), la lista es: {lista}")

# 3. ¡Ahora podemos usar nuestro nuevo método `prepend`!
#    Esto nos permite añadir un elemento al principio de la lista de forma más legible.
lista.prepend(0)
print(f"Después de usar nuestro método prepend(0), la lista es: {lista}")

# El resultado final demuestra que nuestra lista personalizada tiene tanto
# los métodos antiguos (`append`) como los nuevos que hemos creado (`prepend`).
print(f"\nResultado final: {lista}")

# Verificamos el tipo de nuestro objeto para confirmar que es de nuestra clase `Lista`
# y no una `list` normal.
print(f"El tipo de nuestro objeto es: {type(lista)}")
