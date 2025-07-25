# --- Anulación de Métodos (Method Overriding) ---
# La anulación de métodos es una característica de la herencia que permite a una clase hija (subclase)
# proporcionar una implementación específica de un método que ya está definido en su clase padre (superclase).

# Definimos la clase padre 'Ave'.
class Ave:
    # El constructor de la clase 'Ave'.
    def __init__(self):
        # Inicializa un atributo 'volador' para todas las instancias de 'Ave'.
        self.volador = "volador"

    # Define un método llamado 'vuela'. Esta es la implementación base.
    def vuela(self):
        print("vuela ave")

# Definimos la clase hija 'Pato' que hereda de 'Ave'.
class Pato(Ave):
    # El constructor de la clase 'Pato'.
    def __init__(self):
        # --- Llamada al constructor de la clase padre ---
        # 'super()' es una función especial que nos da acceso a los métodos de la clase padre (Ave).
        # Al llamar a 'super().__init__()', nos aseguramos de que el constructor de 'Ave' se ejecute.
        # Esto es crucial para que el atributo 'self.volador' se inicialice también en los objetos 'Pato'.
        super().__init__()
        
        # Añadimos un nuevo atributo específico para la clase 'Pato'.
        self.nada = "nadador"

    # --- Anulación del método 'vuela' ---
    # Aquí estamos "anulando" o "sobrescribiendo" el método 'vuela' de la clase 'Ave'.
    # Cuando se llame a 'vuela()' en un objeto de tipo 'Pato', se ejecutará esta versión del método,
    # en lugar de la versión definida en la clase 'Ave'.
    def vuela(self):
        print("vuela pato")

# --- Demostración ---

# Creamos una instancia de la clase 'Pato'.
pato = Pato()

# Al llamar a 'pato.vuela()', se invoca el método 'vuela' definido en la clase 'Pato',
# porque lo ha anulado.
pato.vuela()  # Salida esperada: vuela pato

# Imprimimos los atributos del objeto 'pato'.
# 'pato.volador' existe gracias a que llamamos a 'super().__init__()' en el constructor de 'Pato'.
# 'pato.nada' existe porque lo definimos directamente en el constructor de 'Pato'.
print(pato.volador, pato.nada)  # Salida esperada: volador nadador
