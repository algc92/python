#se pueden llenar con cualquier dato
lista = ['Python', 120, 'Nombre', 3.14, 6.28]

#saber el tipo de dato
print("Tipo de dato:",type(lista),"\n")

#imprimes la posición de la lista
print("posición 3 de la lista:",lista[3],"\n")

#para saber la cantidad de elementos en la lista
print("tamaño de la lista:",len(lista),"\n")

#modificar el valor de la lista
print("valores de la lista original:",lista,"\n")
lista[0] = "python"
print("valores de la lista modificada:",lista)