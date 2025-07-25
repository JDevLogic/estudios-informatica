# === Invocar o Lanzar Excepciones Manualmente ===
#
# A veces, no queremos que Python lance una excepción por sí solo (como al dividir por cero).
# Queremos ser nosotros quienes, bajo ciertas condiciones lógicas, decidamos que algo
# ha ido mal y que el programa debe detenerse o ser manejado de una forma especial.
# Para esto, usamos la palabra clave `raise`.

# --- Definición de una Función que Lanza una Excepción ---

def division(n=0):
    """
    Esta función calcula la división de 5 entre un número n.
    Pero antes de realizar la operación, comprueba si el divisor es válido.

    Args:
        n (int, optional): El número por el cual se dividirá. Por defecto es 0.

    Raises:
        ZeroDivisionError: Se lanza esta excepción si el argumento `n` es 0.
    """
    # 1. Validación de la Condición de Error
    # Aquí está nuestra lógica de negocio. Decidimos que dividir por cero no es
    # una operación válida en el contexto de nuestra función.
    if n == 0:
        # 2. Lanzamiento Manual de la Excepción
        # Si la condición se cumple, usamos `raise` para crear y lanzar una instancia
        # de una excepción. En este caso, `ZeroDivisionError` es la más apropiada.
        # El texto que pasamos al crear la excepción es el mensaje de error que
        # se mostrará al usuario o que podremos capturar más adelante.
        raise ZeroDivisionError("No se puede dividir por cero. Por favor, proporciona un número diferente.")

    # 3. Ejecución Normal
    # Si la condición de error no se cumple (es decir, `n` no es 0),
    # la función continúa su ejecución normal y devuelve el resultado.
    return 5 / n

# --- Manejo de la Excepción Lanzada ---

# Ahora, vamos a llamar a nuestra función. Como sabemos que PUEDE lanzar una excepción,
# la envolvemos en un bloque `try...except` para manejar el posible error de forma controlada.
try:
    # Intentamos llamar a la función con su valor por defecto (n=0),
    # lo que sabemos que provocará que se lance la excepción.
    resultado = division()
    print(f"El resultado es: {resultado}") # Esta línea nunca se ejecutará en este caso.

# Capturamos específicamente la excepción `ZeroDivisionError`.
# La variable `e` contendrá la instancia de la excepción que creamos con `raise`,
# incluyendo el mensaje de error que le pasamos.
except ZeroDivisionError as e:
    # En lugar de que el programa se detenga con un error feo,
    # mostramos un mensaje amigable al usuario.
    print(f"Error controlado: {e}")
    print("El programa puede continuar después de este bloque...")

# Ejemplo de un caso sin error:
try:
    resultado_ok = division(10)
    print(f"\nLlamada exitosa: El resultado de dividir 5 entre 10 es: {resultado_ok}")
except ZeroDivisionError as e:
    print(f"Este mensaje no debería aparecer: {e}")
