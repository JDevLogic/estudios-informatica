# Ejemplo de operadores logicos

"""              
a = 10 
b = 5
c = 3

# AND (ambas condiciones deben de ser TRUE)
print("¿a es mayor que b y b es mayor que c?", a > b and b > c)

# OR (al menos una condicion debe de ser TRUE)
print("¿a es menor que b o b es mayor que c?", a < b or b > c)

# NOT (niega el resultado)
print("¿No es cierto que a es mayor que b?",not (a > b))"

"""


# Ejercicio extra 

primer_numero = int(input("Introduce el primero numero: "))
segundo_numero = int(input("Introduce el segundo numero: "))

print("¿Ambos son numeros positivos?", primer_numero > 0 and segundo_numero > 0 )
print("¿Al menos uno es negativo?", primer_numero < 0 or segundo_numero < 0 )