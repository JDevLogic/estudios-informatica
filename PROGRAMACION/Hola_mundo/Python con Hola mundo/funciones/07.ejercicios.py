def no_space(texto):                                        # Creamos una funcion que recibe un texto y devuelve el texto sin espacios
    """
    Esta funcion recibe un texto y devuelve el texto sin espacios
    """
    nuevo_texto = ""                                        # Creamos una variable vacia para almacenar el texto sin espacios
    for char in texto:                                      # Recorremos el texto
        if char != " ":                                     # Si el caracter no es un espacio
            nuevo_texto += char                             # Añadimos el caracter al nuevo texto
    return nuevo_texto                                      # Devolvemos el nuevo texto sin espacios

def reverse(texto):                                         # Creamos una funcion que recibe un texto y devuelve el texto al reves 
    """
    Esta funcion recibe un texto y devuelve el texto al reves
    """
    texto_al_reves = ""                                     # Creamos una variable vacia para almacenar el texto al reves    
    for char in texto:                                      # Recorremos el texto  
        texto_al_reves = char + texto_al_reves              # Añadimos el caracter al principio del texto al reves
    return texto_al_reves


def es_palindromo(texto):                                   # Creamos una funcion que recibe un texto y devuelve True si es un palindromo y False si no lo es4
    """
    Esta funcion recibe un texto y devuelve True si es un palindromo y False si no lo es
    """
    texto = no_space(texto)
    texto_al_reves = reverse(texto)
    return texto.lower() == texto_al_reves.lower()

print (es_palindromo("amo la paloma"))
print (es_palindromo("hola mundo"))
print (es_palindromo("Somos o no somos"))