try:                                                        # Intentamos ejecutar el código dentro del bloque try
    print("Hola, mundo!")
    n1 = int(input("Introduce primer número: "))            

except ValueError:                                          # Capturamos la excepción ValueError
    print("Ocurrio un error :(")                            # Mensaje de error personalizado
