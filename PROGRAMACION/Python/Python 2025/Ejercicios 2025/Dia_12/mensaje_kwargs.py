def mensaje_personalizado (**kwargs):                                                 # Creamos una funcion que recibe un numero indefinido de argumentos con nombre tipo diccionario (**kwargs)
    
    destinatario = kwargs.get("destinatario")                                         # Obtenemos el destinatario del diccionario kwargs
    asunto = kwargs.get("asunto")                                                     # Obtenemos el mensaje del diccionario kwargs
    cuerpo = kwargs.get("cuerpo")                                                     # Obtenemos el cuerpo del mensaje del diccionario kwargs
    firma = kwargs.get("firma")                                                       # Obtenemos la firma del mensaje del diccionario kwargs
    
    if not destinatario or not asunto or not cuerpo:                                  # Si no hay destinatario, asunto o cuerpo
            print("Error: Faltan datos para enviar el mensaje")                       # Imprimimos un mensaje de error
            return                                                                    # Retornamos
    
    print (f"\n Para: {destinatario}")                                                # Imprimimos el destinatario
    
    if asunto:                                                                        # Si hay asunto
            print (f" Asunto: {asunto}")                                              # Imprimimos el asunt
    
    print (f"\n {cuerpo}\n")                                                          # Imprimimos el cuerpo
    
    if firma:                                                                         #  Si hay firma
        print (f" - {firma}")                                                         # Imprimimos la firma
    else:                                                                             # Si no hay firma
        print (" - Sin firma")                                                        # Imprimimos sin firma

mensaje_personalizado (destinatario="Lucia", asunto="Hola", cuerpo="¿Cómo estás?", firma="Jonathan")                    # Llamamos a la funcion mostrando diferentes tipos de argumentos con nombre
