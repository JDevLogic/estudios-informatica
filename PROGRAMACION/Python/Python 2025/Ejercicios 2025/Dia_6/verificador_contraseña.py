while True:                                                      # Creamos el bucle con while

    contraseña = str(input("Escribe tu contraseña: "))           # Creamos un variable contraseña que es la que escribara el usuario

    if contraseña.strip() == "python123":                        # Una condicion que con .strip() borra los espacios y que python123 sea la contraseña para entrar
        print("¡Bienvenido!")                                    # El mensaje que se imprimira al poner bien la contraseña
        break                                                    # Con break se acaba el bucle 

    else:                                                           # Si falla se le imprimira un mensaje 
        print("Contraseña incorrecta. Inténtalo de nuevo.")         # El mensaje de que es incorrecta y hasta que no la ponga bien no se acaba el bucle