# Modificar los datos de una lista
lista = ["Python", 24, "Java", "MongoDB", 2025]

print("Lista original:",lista,"\n")

posicion = lista.index("MongoDB")

lista[posicion] = "MONGODB"

print("Lista modificada:",lista)


# Elimina el ultimo elemento de la lista
lista.pop()
print("Lista modificada:",lista)


# para eliminar un elemento en especifico
lista.remove(24)
print("Lista modificada:",lista)