# --- Herencia Múltiple en Python ---
# La herencia múltiple permite que una clase (hija) herede atributos y métodos de más de una clase (padre).
# Aunque es una herramienta poderosa, puede introducir complejidad y problemas si no se maneja con cuidado.

# Definimos varias clases base, cada una con una habilidad específica.
class Caminador:
    def caminar(self):
        print("caminando")

    # Añadimos un método con un nombre genérico para ilustrar el problema de colisión.
    def moverse(self):
        print("Moviéndose por tierra")

class Volador:
    def volar(self):
        print("volando")

    # Esta clase también tiene un método 'moverse'.
    def moverse(self):
        print("Moviéndose por el aire")

class Nadador:
    def nadar(self):
        print("nadando")

# --- El Problema de Colisión de Métodos y el MRO ---
# La clase 'Pato' hereda de las tres clases anteriores.
# El orden en que se listan las clases padre es CRUCIAL.
# Python determina el orden de búsqueda de métodos usando un algoritmo llamado C3 o MRO (Method Resolution Order).
# El MRO define una secuencia lineal y predecible de las clases a seguir.
class Pato(Volador, Caminador, Nadador):
    def programar(self):
        print("programando")

# --- Demostración del MRO (Method Resolution Order) ---
pato = Pato()

# Cuando llamamos a un método que existe en múltiples clases padre, como 'moverse()', 
# Python sigue el MRO de la clase 'Pato'.
# El MRO para 'Pato' será: Pato -> Volador -> Caminador -> Nadador -> object.
# Por lo tanto, se ejecutará el método 'moverse' de la clase 'Volador' porque es la primera que encuentra en esa secuencia.
pato.moverse() # Salida esperada: Moviéndose por el aire

# Si el orden de herencia fuera Pato(Caminador, Volador, Nadador), la salida sería "Moviéndose por tierra".

# Puedes inspeccionar el MRO de una clase para entender el orden de búsqueda:
print("El Orden de Resolución de Métodos (MRO) para la clase Pato es:")
print(Pato.__mro__)

# --- Conclusión ---
# El principal inconveniente de la herencia múltiple es la ambigüedad que puede surgir
# cuando varias clases padre implementan un método con el mismo nombre (el "problema del diamante" es un caso clásico de esto).
# Python lo resuelve de manera determinista con el MRO, pero como programador, debes ser consciente
# del orden de herencia para evitar comportamientos inesperados.
# A menudo, se prefieren alternativas como la composición o el uso de "Mixins" para añadir funcionalidades sin crear jerarquías de herencia complejas.