intentos = 0                                                                         # Para contar los intentos creamos una variable

while True:                                                                          # Creamos un bucle
   
    print("1. Ver perfil")                                                           # Las opciones del bucle
    print("2. Configuracion")
    print("3. Salir")

    opcion = input("Eligue una opcion: ")                                            # Tiene que elegir entre las opciones si falla se le contara 1 intento

    if opcion == "1":                                                                # Si elige la opcion 1 se le dira la opcion que escogio y el numero de intentos
        print(f"Elegiste la opcion 1. Lo lograste en {intentos} intentos. ")
        break                                                                        # Y se rompera el bucle

    elif opcion == "2":                                                              # Lo mismo para las demas opciones
        print(f"Elegiste la opcion 2. Lo lograste en {intentos} intentos. ")
        break

    elif opcion == "3":
        print(f"Elegiste la opcion 3. Lo lograste en {intentos} intentos. ")
        break

    else:                                                                            # Esto es cuando no eligue una opcion del menu
        print("Esta opcion no es valida. ")                                          # Se le dira que no es valida 
        intentos += 1                                                                # Se contara mas 1 los intentos para luego imprimir el numero exacto de intentos