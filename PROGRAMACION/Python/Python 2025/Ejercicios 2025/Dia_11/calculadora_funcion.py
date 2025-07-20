# Crearemos una calculadora simple que realice las operaciones de suma, resta, multiplicacion y division en una sola funcion
# Creamos una funcion que reciba dos numeros y una operacion y dependiendo de la operacion que le pasemos, nos realice la operacion correspondiente

def calcular(num1, num2, operacion):                                # Definimos la funcion calcular con 3 argumentos 

    if operacion == "+":                                            # Definimos la suma 
        return num1 + num2                                          # Retornamos la suma de los dos numeros

    elif operacion == "-":                                          # Definimos la resta
        return num1 - num2                                          # Retornamos la resta de los dos numeros

    elif operacion == "*":                                          # Definimos la multiplicacion
        return num1 * num2                                          # Retornamos la multiplicacion de los dos numeros
    
    elif operacion == "/":                                          # Definimos la division
        if num2 == 0:                                               # Si el segundo numero es cero, retornamos un mensaje de error
            return "Error: Division por cero"
        else:                                                       # Si el segundo numero no es cero, retornamos la division de los dos numeros
            return num1 / num2                                      # Retornamos la division de los dos numeros
    
    else:                                                           # Si la operacion no es valida, retornamos un mensaje de error
        return "Error: Operacion no valida"                         # El mensaje de error 
    

print (calcular(10, 5, "+"))  # Suma
print (calcular(10, 5, "-"))  # Resta
print (calcular(10, 5, "*"))  # Multiplicacion
print (calcular(10, 5, "/"))  # Division
print (calcular(10, 0, "/"))  # Division por cero
print (calcular(10, 5, "^"))  # Operacion no valida
