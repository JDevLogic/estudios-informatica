# Ejercicio 1: Verificacion de Tweets 
# Descripcion: El programa solicita al usuario que ingrese un tweet y verifica si cumple con el límite de 20 caracteres.
# Si el tweet es válido, se imprime un mensaje de éxito. Si no, se imprime un mensaje de error.

tweet = input("Escribe un tweet (máximo 20 caracteres): ")          # Pedimos al usuario que ingrese un tweet

if len(tweet) == 0:                                                 # Si el tweet está vacío      
    print("Error: El tweet no puede estar vacío.")

elif len(tweet) <= 20:                                              # Verificamos si el tweet tiene 20 caracteres o menos
    print("Tweet enviado con éxito.")

else:                                                               # Si el tweet excede el límite de 20 caracteres  
    print("Error: El tweet excede el límite de 20 caracteres.")


# Ejercicio 2: Conversor de Divisas
# Este programa convierte una cantidad de dinero de una divisa a otras. 
# Divisas soportadas: USD (dolares estadounidenses), EUR (euros)y MXN (pesos mexicanos).
# El usuario ingresa la cantidad y la divisa de origen, y el programa calcula la cantidad equivalente en las otras divisas.


cantidad = float(input("Ingrese la cantidad de dinero: "))                              # Pedimos al usuario que ingrese la cantidad de dinero
divisa_origen = input("Ingrese la divisa de origen (USD, EUR, MXN): ").upper()          # Pedimos al usuario que ingrese la divisa de origen

# Tasas de conversion
tasa_usd_eur = 0.95
tasa_usd_mxn = 20.28
tasa_eur_mxn = 21.36

if divisa_origen == "USD":                                                              # Si la divisa de origen es USD
    cantidad_eur = cantidad * tasa_usd_eur                                              # Convertimos a EUR
    cantidad_mxn = cantidad * tasa_usd_mxn                                              # Convertimos a MXN
    print(f"{cantidad} USD son {cantidad_eur:.2f} EUR y {cantidad_mxn:.2f} MXN.")       # Imprimimos el resultado

elif divisa_origen == "EUR":                                                            # Si la divisa de origen es EUR
    cantidad_usd = cantidad / tasa_usd_eur                                              # Convertimos a USD
    cantidad_mxn = cantidad * tasa_eur_mxn                                              # Convertimos a MXN
    print(f"{cantidad} EUR son {cantidad_usd:.2f} USD y {cantidad_mxn:.2f} MXN.")       # Imprimimos el resultado

elif divisa_origen == "MXN":                                                            # Si la divisa de origen es MXN
    cantidad_usd = cantidad / tasa_usd_mxn                                              # Convertimos a USD
    cantidad_eur = cantidad / tasa_eur_mxn                                              # Convertimos a EUR
    print(f"{cantidad} MXN son {cantidad_usd:.2f} USD y {cantidad_eur:.2f} EUR.")       # Imprimimos el resultado

else:                                                                                   # Si la divisa de origen no es válida
    print("Error: Divisa no válida. Por favor, ingrese USD, EUR o MXN.")                # Imprimimos un mensaje de error


# Ejercicio 3: Formateador de Nombres
# Este programa solicita al usuario su nombre completo y lo formatea elimanando espacios adiciocinales y capitalizando las palabras.

nombre = input ("Ingrese su primer nombre: ")                            # Pedimos al usuario que ingrese su nombre

segundo_nombre = input ("Ingrese su segundo nombre: ")                   # Pedimos al usuario que ingrese su segundo nombre

primer_apellido = input ("Ingrese su primer apellido: ")                 # Pedimos al usuario que ingrese su apellido

segundo_apellido = input ("Ingrese su segundo apellido: ")               # Pedimos al usuario que ingrese su segundo apellido

nombre_completo = f"{nombre} {segundo_nombre} {primer_apellido} {segundo_apellido}"                         # Concatenamos los nombres y apellidos 
nombre_completo = nombre_completo.replace("  ", " ")                                                        # Reemplazamos espacios dobles por uno solo
nombre_completo = nombre_completo.strip()                                                                   # Eliminamos espacios adicionales al principio y al final
nombre_completo = nombre_completo.title()                                                                   # Capitalizamos cada palabra

print(f"{nombre_completo}")                                                                                 # Imprimimos el nombre completo 


# Ejercicio 4: Lanzamiento de Dados
# # Simula el lanzamiento de un dado un numero especifico de veces y calcula la frecuencia o porcentaje de cada cara.

# import random                                                                         # Importamos la libreria random para generar numeros aleatorios

# num_lanzamientos = int(input("Ingrese el número de lanzamientos: "))                  # Pedimos al usuario que ingrese el número de lanzamientos

# if num_lanzamientos <= 0:                                                             # Si el número de lanzamientos es menor o igual a 0    
#     print("Error: El número de lanzamientos debe ser mayor a 0.")                     # Imprimimos un mensaje de error
#     exit()                                                                            # Salimos del programa

# resultados = [0] * 6                                                                  # Creamos una lista para almacenar los resultados de cada cara del dado

# for _ in range(num_lanzamientos):                                                     # Repetimos el lanzamiento el número de veces especificado
#     cara = random.randint(1, 6)                                                       # Generamos un número aleatorio entre 1 y 6
#     resultados[cara - 1] += 1                                                         # Incrementamos el contador de la cara correspondiente

# if num_lanzamientos == 1:                                                             # Si solo se lanza una vez 
#     print(f"Salio la cara: {cara}")                                                   # Imprimimos el resultado

# else:                                                                                 # Si se lanzan varias veces
#     for i in range(6):                                                                # Recorremos las caras del dado
#         porcentaje = (resultados[i] / num_lanzamientos) * 100                         # Calculamos el porcentaje de cada cara
#         print(f"Porcentaje de veces que salio la cara {i + 1}: {porcentaje:.2f}%")    # Imprimimos el porcentaje de cada cara


# Ejercicio 5: Caja Registradora
# Este programa simula una caja registradora que acumula el precio de los productos ingresados por el usuario.

total = 0.0                                                                             # Inicializamos el total a 0

while True:                                                                             # Iniciamos un bucle infinito
    precio = input("Ingrese el precio del producto (o 'fin' para terminar): ")          # Pedimos al usuario que ingrese el precio del producto
    if precio.lower() == "fin":                                                         # Si el usuario ingresa "fin"
        break                                                                           # Salimos del bucle
   
    total += float(precio)                                                              # Sumamos el precio del producto al total

    print(f"El total a pagar es: {total:.2f} €")                                        # Imprimimos el total acumulado, formateado a 2 decimales con :.2f




# Ejercicio 6: Calculo de Cambio
# Este programa calcula el cambio que debe darse al cliente segun el pago y el total de la cuenta.

total_cuenta = float(input("Ingrese el total de la cuenta: "))                                  # Pedimos al usuario que ingrese el total de la cuenta

pago_cliente = float(input("Ingrese el pago del cliente: "))                                    # Pedimos al usuario que ingrese el pago del cliente

if total_cuenta <= 0 or pago_cliente <= 0:                                                      # Si el total de la cuenta o el pago del cliente son menores o iguales a 0
    print("Error: El total de la cuenta y el pago del cliente deben ser mayores a 0.")          # Imprimimos un mensaje de error
    exit()                                                                                      # Salimos del programa

if pago_cliente == total_cuenta:                                                                # Si el pago del cliente es igual al total de la cuenta
    print("El cliente ha pagado la cantidad exacta. No hay cambio.")                            # Imprimimos un mensaje indicando que no hay cambio

elif pago_cliente < total_cuenta:                                                               # Si el pago del cliente es menor que el total de la cuenta
    falta = total_cuenta - pago_cliente                                                         # Calculamos la cantidad que falta
    print (f"El cliente ha pagado menos. Faltan {falta:.2f} €")                                 # Imprimimos un mensaje indicando que falta dinero

else:
    cambio = pago_cliente - total_cuenta                                                       # Calculamos el cambio a devolver
    print(f"El cambio a devolver es: {cambio:.2f} €")                                          # Imprimimos el cambio a devolver, formateado a 2 decimales con :.2f