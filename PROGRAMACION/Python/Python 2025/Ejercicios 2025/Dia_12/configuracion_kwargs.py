def mostrar_configuracion (**kwargs):                                                 # Creamos una funcion que recibe un numero indefinido de argumentos con nombre tipo diccionario (**kwargs)
    
    for clave, valor in kwargs.items():                                               # Recorremos los argumentos con un for y con items para que nos de la clave y el valor
            
            if True:                                                                  # Si el valor es True
                print(f"\n Configuracion activada {clave} : {valor}")                 # Imprimimos la clave y el valor
            
            elif valor == False:                                                      # Si el valor es False
                 pass                                                                 # No hacemos nada   

mostrar_configuracion (modo_oscuro=True, notificaciones=False, auto_guardado=True)    # Llamamos a la funcion mostrando diferentes tipos de argumentos con nombre             