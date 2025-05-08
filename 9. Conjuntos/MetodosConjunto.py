# Se recomienda utilizarlo de esta forma ya que se puede causar confusión 
# un conjunto no muestra datos repetidos y la lista si
conjunto = {1, 1, 2, 2, 3, 4, 5}
lista = [1, 1, 2, 3, 4, 5]

print("Lista:",lista)
print("Original:",conjunto)

#añadir un elemento al conjunto
conjunto.add(20)
print("Añade un elemento:",conjunto)

#eliminar y el parametro es el valor a eliminar
conjunto.remove(1)
print("Elimina un elemento especificado:",conjunto)

#elimina al azar un elemento
conjunto.pop()
print("Elimina al azar:",conjunto)

#permite añadir elementos iterables
conjunto.update([5, 6, 7])
print("Update:",conjunto)

#Limpia el conjunto
conjunto.clear()
print("Limpiar:",conjunto)
