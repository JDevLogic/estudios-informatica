# Una función es un bloque de código que se puede reutilizar.
# Se crea con 'def' y se puede recibir datos llamados 'parámetros'.
# 'return' sirve para devolver un resultado y usarlo fuera de la función.
# Ventajas: organizar el código, evitar repetir y hacerlo más fácil de leer.




def saludar ():                             # Se crea la funcion con "def" y el nombre en este caso saludar
    print("Hola Jonathan")                  # Lo que quieres que haga la funcion (en este caso es un mensaje de saludo)

saludar()                                   # Y asi cuando pongas el nombre de la funcion y los parentesis te saldra lo que queremos que haga la funcion.





def obtener_nombre ():                      # Creamos la funcion nombre 
    return "Jonathan"                       # return es para que guarde un valor (en este caso Jonathan)


nombre = obtener_nombre()                   # Para que imprima el valor que creamos
print("Tu nombre es:",nombre)               # El mensaje que saldra 





def saludar(nombre):                        # Creamos la funcion saludar entre parentesis el "parametro"
    print("Hola",nombre)                    # El mensaje para saludar en este caso

saludar ("Jonathan")                        # Aqui entre parentesis ponemos el "argumento" es el dato en este caso un nombre 
saludar ("Lucia")
saludar ("Bryan")





def sumar (num1, num2):                                 # Creamos un funcion para que dos numero se sumen
    return num1 + num2                                  # Hacemos que los dos numeros se sumen y guardamos su valor con "return"


resultado = sumar(2,3)                                  # Aqui ponemos que resultado sea igual a la funcion sumar ponemos 2 argumentos (2 numeros) 

print("El resultado de la suma es:",resultado)          # Y los suma e imprime el resultado con este mensaje 





def pedir_nombre():                                     # Creamos la funcion para pedir nombre 
    nombre = input ("Introduce tu nombre: ")            # Creamos una variable llamada nombre y pedimos que nos lo diga el usuario
    print("Hola,",nombre)                               # Aqui sale el saludo con el nombre que nos da el usuario

pedir_nombre()                                          # Para llamar a la funcion ponemos "pedir_nombre()" 




def sumar_numeros():                                                  # Creamos una funcion para sumar numeros
    num1 = float(input ("Introduce el primer numero: "))              # Pedimos al usuario el primer numero y lo convierte en float (decimales)
    num2 = float(input ("Introduce el segundo numero: "))             
    resultado = num1 + num2                                           # Hacemos que el num1 y el num2 se sumen y el valor sea el resustado
    print ("El resultado de la suma es: ",resultado)                  # El mensaje del resultado 

sumar_numeros()                                                       # Llamamos a la funcion sin esto no funcionaria