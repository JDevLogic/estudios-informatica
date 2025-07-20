# Conversion de tipos de datos en Python 

edad = "21"         # Cadena de texto
altura = "1.75"     # Cadena de texto

# Convertir texto a numero entero 
edad_numero = int(edad)

# Convertir texto a numero decimal
altura_numero = float(altura)

# Convertir numero a texto
edad_texto = str(edad_numero)

# Convertir numero a booleano (1 es True, 0 es False)
es_mayor = bool(edad_numero)

# Imprimir los valores convertidos y sus tipos
print("Edad como numero:", edad_numero, "-> Tipo:", type(edad_numero))
print("Altura como numero:", altura_numero, "-> Tipo:", type(altura_numero))
print("Edad como texto:", edad_texto, "-> Tipo:", type(edad_texto))
print("¿Es mayor de edad?", es_mayor, "-> Tipo:", type(es_mayor))