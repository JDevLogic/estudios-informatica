n1 = input ("Introduzca el primer numero: ")                # Solicita el primer número al usuario
n2 = input ("Introduzca el segundo numero: ")               # Solicita el segundo número al usuario

n1 = int(n1)                                                # Convierte el primer número a entero
n2 = int(n2)                                                # Convierte el segundo número a entero

suma = n1 + n2                                              # Suma los dos números
resta = n1 - n2                                             # Resta los dos números
multiplicacion = n1 * n2                                    # Multiplica los dos números
division = n1 / n2                                          # Divide los dos números

mensaje = f"""
Para los numeros {n1} y {n2},
el resultado de la suma es: {suma}
el resultado de la resta es: {resta}
el resultado de la multiplicacion es: {multiplicacion}
el resultado de la division es: {division}
"""

print (mensaje)                                              # Imprime el mensaje con los resultados