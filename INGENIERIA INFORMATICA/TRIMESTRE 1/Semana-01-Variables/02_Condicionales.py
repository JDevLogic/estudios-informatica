edad = int(input("¿Cuantos años tienes? "))

if edad >= 18:
    print("Eres mayor de edad.")

else:
    print("Eres menor de edad.")



nota = float(input("Introduce tu nota: "))

if nota >= 9:
    print("Sobresaliente")

elif nota >= 7:
    print("Notable")

elif nota >= 5:
    print("Aprobado")

else:
    print("Suspenso")


# EJERCICIOS DEL DIA 

# Pregunta al usuario su edad.
# Si tiene 18 o más, muestra "Bienvenido, adulto".
# Si tiene entre 13 y 17, muestra "Adolescente detectado"
# Si tiene menos de 13, muestra "Demasiado joven, acceso denegado".
# Pide al usuario que escriba una contraseña.
# Si coincide con "python123", dile "Acceso concedido".
# Si no coincide, dile "Contraseña incorrecta".
# Pregunta al usuario una nota del 0 al 10.
# Imprime el tipo de nota (como en el ejemplo anterior).


edad = int (input("Cual es tu edad? "))

if edad >= 18:
    print("Bienvenido, adulto")

elif edad >= 13:
    print("Adolescente detectado. ")

else:
    print("Demasiado joven, acceso denegado")



contraseña = "python123"

contra = input("Introduzca su contraseña: ")

if contra == contraseña:
    print("Acceso concedido.")

else:
    print("Acceso denegado.")
    

notas = float(input("Introduzca tu nota: "))

if notas>= 9:
    print("Sobresaliente")

elif notas >=7:
    print("Notable")

elif notas >=5:
    print("Aprobado")

else:
    print("Suspenso")


    