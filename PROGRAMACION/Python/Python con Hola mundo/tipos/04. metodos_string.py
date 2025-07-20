# Estos son algunos de los métodos más comunes para manipular cadenas en Python

animal = "    chanCHIto feliz    "

print (animal.upper())                  # Convierte a mayúsculas

print (animal.lower())                  # Convierte a minúsculas    

print (animal.strip().capitalize())     # Combina eliminar espacios y convertir a mayúscula la primera letra

print (animal.title())                  # Convierte la primera letra de cada palabra a mayúscula

print (animal.strip())                  # Elimina los espacios en blanco al principio y al final

print (animal.lstrip())                 # Elimina los espacios en blanco de la izquierda

print (animal.rstrip())                 # Elimina los espacios en blanco de la derecha

print (animal.find("CH"))               # Busca la posición de la primera aparición de "CH"

print (animal.find("cH"))               # Nos devuelve -1 porque no encuentra "cH"

print (animal.replace("CH", "ch"))      # Reemplaza "CH" por "ch"

print ("CH" in animal)                  # Devuelve True si "CH" está en la cadena