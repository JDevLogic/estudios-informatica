contador = 0 

while contador <5:
    print("Contador: ", contador)

    contador += 1

while True:
    respuesta = (input ("Escribe 'salir' para terminal: "))

    if respuesta == 'salir':
        break


intentos = 0 

while intentos < 3:
    
    contra = input("Introduce la contraseña: ")

    if contra == "python123":
        print("Contraseña correcta!!")
        break

    else:
        print("Contraseña incorrecta. ")
        
        intentos += 1
        

# EJERCICIOS DEL DIA 

# Contraseña con intentos
# El usuario tiene 3 intentos para escribir correctamente "backend".
# Si acierta, muestra "Bienvenido al sistema".
# Si falla 3 veces, muestra "Bloqueado por seguridad".

# Menú interactivo.

# Crea un menú que muestre:
# 1. Saludar
# 2. Decir mi edad
# 3. Salir


# Según lo que escriba el usuario, debe hacer lo correspondiente.
# El menú debe repetirse hasta que el usuario pulse 3.
# Contador personalizado
# Pide al usuario un número.
# Muestra todos los números desde 1 hasta ese número usando un while.


contra='backend'

intentos = 0

while intentos < 3:
    contraseña = input ("Introduce la contraseña: ")
    
    if contraseña == contra:
        print("Bienvenida al sistema")
        break

    else:
        intentos += 1
        
        if intentos < 3:
            print("Contraseña incorrecta. ")

        else:
            print("Bloqueado por seguridad numero maximo de intentos.")

        
            



while True:

    print ("\n Menu Interactivo: ")

    print("1.Saludar")

    print("2.Decir mi edad")

    print ("3.Salir")

    opcion = int (input("Elige una opcion: "))

    if opcion == 1:
        nombre = input ("Ingresa tu nombre: ")
        print (f"Saludos {nombre}.")

    elif opcion == 2:
        edad = int (input("Ingresa tu edad: "))
        print (f"Tu edad es la de {edad} años")
    
    elif opcion == 3:
        print ("Saliendo... ")
        break





        


