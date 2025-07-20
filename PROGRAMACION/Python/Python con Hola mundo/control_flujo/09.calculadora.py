print("\n Bienvenido a la calculadora")
print(" Para salir de la calculadora, ingrese 'salir' en cualquier momento")
print(" Las operaciones son suma, resta, multi y div")

numero1 = input("Ingresa el primer número: ")                           # Pedimos el primer número
if numero1.lower() == "salir":                                          # Si el usuario ingresa "salir", terminamos el programa
    exit()

numero1 = int(numero1)                                                  # Convertimos el primer número a entero

while True:                                                             # Bucle infinito
    operacion = input("Ingresa operación: ")                            # Pedimos la operación
    if operacion == "salir":                                            # Si el usuario ingresa "salir", salimos del bucle
        break

    numero2 = input("Ingresa el siguiente número: ")                    # Pedimos el siguiente número
    if numero2.lower() == "salir":                                      # Si el usuario ingresa "salir", salimos del bucle
        break

    numero2 = int(numero2)                                              # Convertimos el segundo número a entero

    if operacion.lower() == "suma":                                     # Si la operación es suma
        numero1 +=numero2                                               # Sumamos y actualizamos numero1
    elif operacion.lower() == "resta":                                  # Si la operación es resta
        numero1 -=numero2                                               # Restamos y actualizamos numero1
    elif operacion.lower() == "multi":                                  # Si la operación es multiplicación
        numero1 *= numero2                                              # Multiplicamos y actualizamos numero1
    elif operacion.lower() == "div":                                    # Si la operación es división
        if numero2 == 0:                                                # Verificamos si el divisor es 0
            print("Error: División por cero no permitida")
            continue
        numero1 /= numero2                                              # Dividimos y actualizamos numero1
    else:                                                               # Si la operación no es válida
        print("Operación no válida")                                    # Imprimimos un mensaje de error
        continue                                                        # Continuamos con la siguiente iteración del bucle

    print(f"El resultado es {numero1}")                                 # Imprimimos el resultado (ahora almacenado en numero1)
