from pprint import pprint

string = "Hola mundo este es mi string"

def quita_espacios(texto):
    """
    Esta función recibe un string y devuelve el mismo string pero sin espacios.

    """
    return[char for char in texto if char != " "]

def cuenta_caracteres(lista):
    """
    Esta función recibe un string y devuelve la cantidad de caracteres que tiene.

    """
    chars_dict = {}
    for char in lista:
        
        if char in chars_dict:
            chars_dict[char] += 1

        else:
            chars_dict[char] = 1
    
    return chars_dict

def ordena(dict):
    return sorted(

        dict.items(), 
        key = lambda item: item[1],
        reverse=True
    )

def mayores_tuplas(lista):
    """
    Esta función recibe una lista de tuplas y devuelve la tupla con el mayor valor.

    """
    
    maximo = lista[0][1]

    respuesta = {}

    for orden in lista:
        
        if maximo > orden[1]:
            break
        
        respuesta [orden[0]] = orden[1]
        
    return respuesta

def crea_mensaje(diccionario):
    """
    Esta función recibe un diccionario y devuelve un string con el mensaje.

    """
    mensaje = "Los que mas se repiten son:\n"
    
    for key, value in diccionario.items():
        mensaje += f"- {key} con {value} repeticiones \n"
    
    return mensaje

sin_espacios = quita_espacios(string)

contados = cuenta_caracteres(sin_espacios)          # Cuenta los caracteres del string sin espacios

ordenados = ordena(contados)                        # Ordena el diccionario por la cantidad de caracteres

mayores = mayores_tuplas(ordenados)                 # Devuelve la tupla con el mayor valor

mensaje = crea_mensaje(mayores)                     # Crea el mensaje con los caracteres que mas se repiten

print(mensaje)
