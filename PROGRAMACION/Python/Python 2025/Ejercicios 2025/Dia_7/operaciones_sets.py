backend = {"Python" , "Java" , "Node.js"}

frontend = {"JavaScript" , "React" , "Python"}

print(backend | frontend)           # Para que los sets se unan usamos | 

print(backend & frontend)           # Con & hace una interseccion que saca el elemento igual de cada set

print(backend - frontend)           # Sirve para buscar elementos que no estan en el otro set y los imprime
