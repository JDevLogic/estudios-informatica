tecnologias_usadas = {"Python" , "JavaScript" , "SQL"}                      # Creamos un set que sea de tecnologias usadas 

tecnologias_incompatibles = {"C#" , "PHP" , "Go"}                           # Creamos otro de las tecnologias incompatibles

if tecnologias_usadas.isdisjoint(tecnologias_incompatibles):                # Con isdisjoint sirve para comparar ambos sets y ver si tienen un elemento en comun
    print ("Todo esta bien. No hay tecnologias incompatibles. ")            # Si no tienen en comun sacara el valor boleano TRUE "Todo esta bien"

else:                                                                       # Si tienen en comun pondra sera False 
    print("¡Cuidado! Hay conflicto de tecnologias. ")                       # Este es el mensaje porque tienen en comun entonces hay conflicto 