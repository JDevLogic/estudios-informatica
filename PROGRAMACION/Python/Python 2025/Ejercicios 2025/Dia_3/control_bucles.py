# break -> Rompe el bucle y termina la ejecución del mismo.
# continue -> Salta esa iteración y continúa con la siguiente.
# pass -> No hace nada, sirve como marcador de posición.



for numero in range (1,10):                      # Aqui e hace un recorrido del 1 al 9 
    print("Numero:",numero)                      # Sale el mensaje del recorrido 

    if numero == 5:                              # Crea una condicion de que numero sea igual a 5 
       print("ME DETENGO EN EL 5")               # El mensaje de que se detiene
    break                                        # El break que es literalmente romper (se acabo)



for numero in range (1,10):                      # Hace el recorrido 
     
    if numero == 5:                              # Hace una condicion de que cuando llegue a 5 lo salte 
        print ("Salto el numero 5")              # El mensaje del mismo
        continue                                 # continue para que no se pare del todo sino que se lo salte y siga 

    print ("Numero: ", numero)                   # El codigo para que siga imprimiendo los numeros restantes 




for numero in range (1,6):                       # Recorrido del 1 al 5 
    if numero == 3:                              # Cuando llegue al 3 
        pass                                     # Aqui se pondra luego algo por ahora se pone pass para que no haya error lo salta
    else:                                       
        print("Numero: ",numero)                 # Para que acabe de poner los numero restantes 
