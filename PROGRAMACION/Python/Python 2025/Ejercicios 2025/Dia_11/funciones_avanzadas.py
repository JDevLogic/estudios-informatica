# Creamos una funcion que reciba un argumento por defecto y dependiendo del argumento que le pasemos, nos salude en un idioma diferente

def saludar (idioma = "es"):                    # Definimos la funcion saludar con un argumento por defecto)                                
      
    if idioma == "es":                          # Definimos el idioma español
        print("Hola")                           # Saludo en español

    elif idioma == "en":                        # Definimos el idioma ingles
        print("Hello")                          # Saludo en ingles
    
    else:
        print("Idioma no soportado")            # Si el idioma no es español ni ingles, se imprime un mensaje de error
    
    
saludar()                                      # Llamamos a la funcion sin argumentos, por lo que se ejecutara el idioma por defecto
saludar("en")                                  # Llamamos a la funcion con el argumento "en", por lo que se ejecutara el idioma ingles
saludar("fr")                                  # Llamamos a la funcion con el argumento "fr", por lo que se ejecutara el idioma no soportado