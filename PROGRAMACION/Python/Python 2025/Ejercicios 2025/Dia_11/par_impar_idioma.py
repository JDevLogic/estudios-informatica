# Creamos una funcion que reciba un argumento por defecto y dependiendo del argumento que le pasemos, nos diga si el numero es par o impar 

def par_impar(idioma = "es"):                                   # Definimos la funcion par_impar con un argumento por defecto

    if idioma =="es":                                           # Definimos el idioma español
        
        numero = int(input("Introduce un número: "))            # Solicitamos un número al usuario y lo convertimos a entero
        
        if numero % 2 == 0:                                     # Si el número es divisible entre 2, es par               
            print("El número es par.")                          # Imprimimos que el número es par
        else:                                                   # El else se ejecuta si el número no es divisible entre 2      
            print("El número es impar.")                        # Si no es divisible entre 2, es impar
    
    elif idioma == "en":                                        # Definimos el idioma ingles

        numero = int(input ("Enter a number: "))                # Solicitamos un número al usuario y lo convertimos a entero (en ingles)

        if numero % 2 == 0:
            print("The number is even.")
        else:
            print("The number is odd.")
    
    else:                                                       # Si el idioma no es español ni ingles, se imprime un mensaje de error                            
        print("Idioma no soportado")                            # El mensaje de error se imprime en español

par_impar()                                                     # Llamamos a la funcion sin argumentos, por lo que se ejecutara el idioma por defecto
par_impar("en")                                                 # Llamamos a la funcion con el argumento "en", por lo que se ejecutara el idioma ingles   
par_impar("fr")                                                 # Llamamos a la funcion con el argumento "fr", por lo que se ejecutara el idioma no soportado