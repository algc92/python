lista = [5, 2, 1, 4, 3]

#cuenta la cantidad de elementos de algun valor en especifico
print("se encontro el elemento",lista.count(5),"veces dentro de la lista\n")

# Busca un elemento y devuelve la posición, solamente se pasa el parametro a buscar y va a retornar el primero que encuentre 
print("Encontrado en la posición:",lista.index(5),"\n")

# Ordenar lista ascendente
print("Lista sin ordenar",lista,"\n")
lista.sort()
print("Lista ordenada ascendente",lista,"\n")

# ordenar descendente
lista.reverse()
print("Lista ordenada descendente",lista,"\n")
