while True:                                                       # Para el menu creamos un bucle
    print("1. Saludar")                                           # Ponemos las opciones que van a estar para el usuario
    print("2. Contar del 1 al 5")
    print("3. Mostrar los pares del 0 al 10")
    print("4. Salir")

    opcion = input("Eligue una opcion: ")                         # Pedimos que eliga una opcion y creamos una variable

    if opcion == "1":                                             # Aqui ponemos que si eligue la opcion 1 cumpla ciertas condiciones 
        nombre = input("Introduce tu nombre: ")                   # Como es saludar se le pedira el nombre al usuario
        print(f"Saludos {nombre}. Bienvenido.")                   # El mensaje de saludo y bienvenida con el nombre que nos ingreso el usuario
    
    elif opcion == "2":                                           # Si eligue la opcion 2 pasara ciertas cosas
        for numero in range (1,6):                                # Como es contar del 1 al 5 se crea un for porque sabemos el inicio y el final del bucle 
            print("Numero: ", numero)                             # Aqui imprimimos los numeros con numero y su variable 

    elif opcion == "3":                                           # Si selecciona la opcion 3 se contara solo los pares
        for numero in range (0,12,2):                             # Se puede conseguir con for es como el recorrido pero al final tiene los saltos que hace y se pone 2 para que salte de 2 en 2 que son los pares 
            print("Numero", numero)                               # Aqui el mensaje que imprimira los mensajes pares
    
    elif opcion == "4":                                           # La opcion 4 sencilla salir 
        print("Saliendo del menu... ")                            # Mensaje de que esta saliendo 
        break                                                     # Con break rompe el bucle para salir
    
    else:                                                         # El else por si no eligen una opcion de las que estan definidas
        print("Opcion invalida. Intentelo de nuevo. ")            # El mensaje de que no es valida la opcion
