# Ejercicio 1: Conversor de Temperatura

# Escribe un programa que convierta temperaturas de Celsius a Fahrenheit y Kelvin.
# La fórmula para convertir Celsius a Fahrenheit es: F = C * 9/5 + 32
# La fórmula para convertir Celsius a Kelvin es: K = C + 273.15

temperatura_celsius = float(input("Introduce la temperatura en Celsius: "))           # Solicita la temperatura en Celsius al usuario

temperatura_fahrenheit = temperatura_celsius * 9/5 + 32                               # Convierte Celsius a Fahrenheit
temperatura_kelvin = temperatura_celsius + 273.15                                     # Convierte Celsius a Kelvin

print (f"La temperatura en Fahrenheit es: {temperatura_fahrenheit:.2f} °F")           # Imprime la temperatura en Fahrenheit, formateada a 2 decimales con :.2f
print (f"La temperatura en Kelvin es: {temperatura_kelvin:.2f} K")                    # Imprime la temperatura en Kelvin, formateada a 2 decimales con :.2f



# Ejercicio 2: Calculadora de Divisas

# Escribe un programa que convierta una cantidad de dinero de una divisa a otra.
# Por ejemplo, de euros a dólares o de libras a yenes.
# Puedes usar tasas de cambio fijas para simplificar el ejercicio.
# Ejemplo de tasas de cambio (puedes modificarlas)
# USD:cantidad * 0.050
# EUR:cantidad * 0.047
# GBP:cantidad * 0.039
# JPY:cantidad * 7.71

moneda_local = input ("Introduce la cantidad de dinero en tu moneda local: ")               # Solicita la cantidad de dinero al usuario

moneda_local = float(moneda_local)                                                          # Convierte la cantidad de dinero a float

# Tasas de cambio (puedes modificarlas)
tasa_cambio_usd = 0.050
tasa_cambio_eur = 0.047
tasa_cambio_gbp = 0.039
tasa_cambio_jpy = 7.71

# Conversión a otras divisas
cantidad_usd = moneda_local * tasa_cambio_usd
cantidad_eur = moneda_local * tasa_cambio_eur
cantidad_gbp = moneda_local * tasa_cambio_gbp
cantidad_jpy = moneda_local * tasa_cambio_jpy

# Imprime los resultados
print (f"La cantidad en USD es: {cantidad_usd:.2f} $")               # Imprime la cantidad en USD, formateada a 2 decimales con :.2f
print (f"La cantidad en EUR es: {cantidad_eur:.2f} €")               # Imprime la cantidad en EUR, formateada a 2 decimales con :.2f
print (f"La cantidad en GBP es: {cantidad_gbp:.2f} £")               # Imprime la cantidad en GBP, formateada a 2 decimales con :.2f
print (f"La cantidad en JPY es: {cantidad_jpy:.2f} ¥")               # Imprime la cantidad en JPY, formateada a 2 decimales con :.2f



# Ejercicio 3: Calculadora de cambio 

# Escribe un programa que calcule el cambio que se debe devolver al cliente después de una compra.

dinero_recibido = float(input("Introduce la cantidad de dinero recibido: "))                 # Solicita la cantidad de dinero recibido al usuario
precio_producto = float(input("Introduce el precio del producto: "))                         # Solicita el precio del producto al usuario

cambio = dinero_recibido - precio_producto                                                   # Calcula el cambio a devolver

print (f"El cambio a devolver es: {cambio:.2f} €")                                           # Imprime el cambio a devolver, formateado a 2 decimales con :.2f-


# Ejercicio 4: Formateador de Nombres
# Este programa asegura que los nombres ingresados por el usuario esten correctamente formateados.

primer_nombre = input("Introduce tu primer nombre: ")                                                               # Solicita el primer nombre al usuario
segundo_nombre = input("Introduce tu segundo nombre: ")                                                             # Solicita el segundo nombre al usuario

primer_apellido = input("Introduce tu primer apellido: ")                                                           # Solicita el primer apellido al usuario
segundo_apellido = input("Introduce tu segundo apellido: ")                                                         # Solicita el segundo apellido al usuario

primer_nombre = primer_nombre.strip().capitalize()                                                                  # Elimina espacios y capitaliza el primer nombre
segundo_nombre = segundo_nombre.strip().capitalize()                                                                # Elimina espacios y capitaliza el segundo nombre
primer_apellido = primer_apellido.strip().capitalize()                                                              # Elimina espacios y capitaliza el primer apellido
segundo_apellido = segundo_apellido.strip().capitalize()                                                            # Elimina espacios y capitaliza el segundo apellido

nombre_completo = f"{primer_nombre} {segundo_nombre} {primer_apellido} {segundo_apellido}".replace("  "," ")        # Combina los nombres y apellidos, eliminando espacios dobles
print (f"Tu nombre completo es: {nombre_completo}")                                                                 # Imprime el nombre completo