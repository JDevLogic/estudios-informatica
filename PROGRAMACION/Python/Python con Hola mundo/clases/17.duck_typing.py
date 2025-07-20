# === Duck Typing: "Si camina como un pato y grazna como un pato, es un pato" ===
#
# En Python, no nos interesa el "tipo" o la "clase" de un objeto, sino lo que
# "puede hacer" (es decir, los métodos que tiene).
# Este principio permite una gran flexibilidad en el diseño de nuestro código.

# --- Definición de Clases con un Comportamiento Común ---

class Perro:
    """
    Una clase que representa a un Perro.
    Tiene un método `saludar` que define su comportamiento.
    """
    def saludar(self):
        print("Guau!")

class Gato:
    """
    Una clase que representa a un Gato.
    También tiene un método `saludar`, como el Perro, pero con un comportamiento diferente.
    """
    def saludar(self):
        print("Miau!")

class Humano:
    """
    Una clase que representa a un Humano.
    Al igual que las otras, "sabe" cómo `saludar`.
    """
    def saludar(self):
        print("Hola!")

class Pato:
    """
    Esta clase también "sabe" saludar. Demuestra que podemos agregar
    nuevos tipos sin cambiar la función que los utiliza.
    """
    def saludar(self):
        print("Cuack!")

# --- Función que Utiliza Duck Typing ---

def hacer_saludar(objeto_que_saluda):
    """
    Esta función es el núcleo del ejemplo de Duck Typing.

    Args:
        objeto_que_saluda: Un objeto cualquiera.

    La función no comprueba de qué clase es el objeto con `isinstance()` o `type()`.
    Simplemente "confía" en que el objeto que se le pasa tiene un método llamado `saludar()`.
    Si el objeto tiene el método, el código funciona. Si no lo tiene, Python lanzará un error.
    """
    print(f"Intentando que un objeto de tipo {type(objeto_que_saluda).__name__} salude...")
    # Aquí está la magia del Duck Typing: llamamos al método sin verificar el tipo.
    objeto_que_saluda.saludar()

# --- Demostración del Funcionamiento ---

print("--- Inicio de la demostración de Duck Typing ---")

# 1. Creamos instancias (objetos) de nuestras diferentes clases.
perro = Perro()
gato = Gato()
humano = Humano()
pato = Pato()

# 2. Usamos la función `hacer_saludar` con cada uno de los objetos.
#    La función funcionará para todos ellos porque todos tienen el método `saludar()`.
#    Son "patos" en el contexto de nuestra función, porque todos "graznan" (saludan).

print("" \
"Llamando a la función con un objeto Perro:")
hacer_saludar(perro)

print("" \
"Llamando a la función con un objeto Gato:")
hacer_saludar(gato)

print("" \
"Llamando a la función con un objeto Humano:")
hacer_saludar(humano)

print("" \
"Llamando a la función con un objeto Pato:")
hacer_saludar(pato)

print("" \
"--- Fin de la demostración ---")

# ¿Qué pasaría si le pasamos un objeto que NO tiene el método saludar?
# Por ejemplo, un número entero.

# numero = 5
# hacer_saludar(numero) # -> Esto daría un AttributeError: 'int' object has no attribute 'saludar'
# El error ocurre porque un entero no "camina como un pato", es decir, no tiene el método que esperamos.