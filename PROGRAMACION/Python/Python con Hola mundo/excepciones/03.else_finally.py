try:                                                        
    print("Hola, mundo!")
    n1 = int(input("Introduce primer número: "))            

except Exception as e:                                         
    print("Ingrese un número válido.")

else:
    print("No se ha producido ningun error.")

finally:
    print("Se ha ejecutado el bloque finally, independientemente de si ocurrió un error o no.")
