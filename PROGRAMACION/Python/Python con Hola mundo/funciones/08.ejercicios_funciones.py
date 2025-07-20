# Ejercicio 1: Aplicar descuento 
# Este ejercicio tiene como objetivo ayudarte a comprender como calcular el total de una cuenta despues de aplicar un descuento.
# Es ideal para practicar operaciones matematicas simples y trabajar con funciones.

# Instrucciones:
# 1. Definir una funcion que tome como parametros el total de una cuenta y un porcentaje de descuento.
# 2. Calcular el monto correspondiente al descuento.
# 3. Restar el descuento del total original.
# 4. Devuelve el total final.

def total_con_descuento(total, descuento):
    """
    Calcula el total después de aplicar un descuento.
    :param total: Total de la cuenta (float).
    :param descuento: Porcentaje de descuento (float).
    """
    monto_descuento = total * (descuento / 100)               # Calculamos el monto del descuento
    total_final = total - monto_descuento                     # Restamos el descuento al total original
    
    return total_final                                        # Devolvemos el total final


total = float(input("Introduce el total de la cuenta: "))                      # Convertimos el total a un numero decimal
descuento = float(input("Introduce el porcentaje de descuento: "))             # Convertimos el descuento a un numero decimal

total_final = total_con_descuento(total, descuento)                            # Llamamos a la funcion y guardamos el resultado en una variable

print(f"El total final despues del descuento es: {total_final}€")               # Imprimimos el resultado



# Ejercicio 2: Conversor de Unidades de Tiempo
# Este ejercicio te permitira practicar como convertir valores entre diferentes unidades de tiempo.
# Es una excelente oportunidada para trabajar con estructuras condicionales y comprender las relaciones entre diferentes unidades de tiempo.

# Instrucciones:
# 1. Definir 3 funciones: a_segundos: Convierte una cantidad y unidad dada a segundos.
                        # de_segundos: Convierte una cantidad en segundos a otra unidad deseada 
                        # convertir_tiempo: Usa las funciones anteriores para realizar una conversion completa entre dos unidades 
# 2. Considera las siguientes unidades:
# 3. segundo, minuto,hora,dia,mes(30 dias), año (365 dias).

def a_segundos(cantidad, unidad):                                   # Creamos la funcion de segundos a otra unidad    
    """
    Convierte una cantidad de tiempo a segundos.
    :param cantidad: Cantidad de tiempo (float).
    :param unidad: Unidad de tiempo (str).
    :return: Cantidad en segundos (float).
    """
    if unidad == "segundo":                                         # Si la unidad es segundos, no hacemos nada  
        return cantidad
    
    elif unidad == "minuto":                                        # Si la unidad es minutos, multiplicamos por 60 
        return cantidad * 60
    
    elif unidad == "hora":                                          # Si la unidad es horas, multiplicamos por 3600   
        return cantidad * 3600
    
    elif unidad == "dia":                                           # Si la unidad es dias, multiplicamos por 86400    
        return cantidad * 86400
    
    elif unidad == "mes":                                           # Si la unidad es meses, multiplicamos por 2592000
        return cantidad * 2592000
    
    elif unidad == "año":                                           # Si la unidad es años, multiplicamos por 31536000 
        return cantidad * 31536000
    else:                                                           # Si la unidad no es valida, lanzamos un error 
        raise ValueError(f"Unidad no válida: {unidad}")
   

def de_segundos(cantidad, unidad):                                  # Creamos la funcion de segundos a otra unidad
    """
    Convierte una cantidad de segundos a otra unidad de tiempo.
    :param cantidad: Cantidad de tiempo en segundos (float).
    :param unidad: Unidad de tiempo (str).
    :return: Cantidad en la unidad deseada (float).
    """
    if unidad == "segundo":                                         # Si la unidad es segundos, no hacemos nada
        return cantidad                                             # Devolvemos la cantidad en segundos
    
    elif unidad == "minuto":                                        # Si la unidad es minutos, dividimos entre 60
        return cantidad / 60                                        # Devolvemos la cantidad en minutos
    
    elif unidad == "hora":                                          # Si la unidad es horas, dividimos entre 3600  
        return cantidad / 3600                                      # Devolvemos la cantidad en horas
    
    elif unidad == "dia":                                           # Si la unidad es dias, dividimos entre 86400
        return cantidad / 86400                                     # Devolvemos la cantidad en dias
    
    elif unidad == "mes":                                           # Si la unidad es meses, dividimos entre 2592000
        return cantidad / 2592000
    
    elif unidad == "año":                                           # Si la unidad es años, dividimos entre 31536000    
        return cantidad / 31536000

    else:                                                           # Si la unidad no es valida, lanzamos un error 
        raise ValueError(f"Unidad no válida: {unidad}")             # Devolvemos un error si la unidad no es valida


def convertir_tiempo(cantidad, unidad_origen, unidad_destino):
    """
    Convierte una cantidad de tiempo de una unidad a otra.
    :param cantidad: Cantidad de tiempo (float).
    :param unidad_origen: Unidad de origen (str).
    :param unidad_destino: Unidad de destino (str).
    :return: Cantidad convertida a la unidad destino (float).
    """
    cantidad_en_segundos = a_segundos(cantidad, unidad_origen)                                              # Convertimos la cantidad a segundos
    
    cantidad_convertida = de_segundos(cantidad_en_segundos, unidad_destino)                                 # Convertimos de segundos a la unidad deseada
    return (f"{cantidad} {unidad_origen}(s) son {cantidad_convertida:.2f} {unidad_destino}(s)")             # Imprimimos el resultado
    

# Entrada del usuario
cantidad = float(input("Introduce la cantidad de tiempo: "))                                                # Convertimos la cantidad a un número decimal
unidad_origen = input("Introduce la unidad de origen (segundo, minuto, hora, dia, mes, año): ").lower()     # Convertimos la unidad a minúsculas
unidad_destino = input("Introduce la unidad de destino (segundo, minuto, hora, dia, mes, año): ").lower()   # Convertimos la unidad a minúsculas

print(convertir_tiempo(cantidad, unidad_origen, unidad_destino))                                            # Llamamos a la función y mostramos el resultado





# Ejercicio 3: Calcular Promedio
# En este ejercicio aprenderas a calcular el promedio de una serie de numeros.
# Tambien trabajaras con parametros variables en funciones.

# Instrucciones:
# 1. Define una funcion que acepte un numero variable de argumentos.
# 2. Si no proporcionas numeros,devuelve 0.
# 3. Si se proporcionan numeros, calcula y devuelve el promedio.

def calcular_promedio(*numeros):
    """
    Calcula el promedio de una serie de números.
    :param numeros: Números a promediar (float).
    :return: Promedio (float) o 0 si no se proporcionan números.
    """
    return sum(numeros) / len(numeros) if numeros else 0                                                # Calculamos el promedio y devolvemos 0 si no hay numeros todo en una sola linea 


numeros = input("Introduce los numeros separados por comas: ")                                          # Pedimos al usuario que introduzca los numeros

print(f"El promedio es: {calcular_promedio(*map(float, numeros.split(',')))}")                          # Llamamos a la funcion y mostramos el resultado
