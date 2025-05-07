# En la siguiente lista, debes hacer un programa que muestre los valores al usuario, 
# a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos 
# en el primer y segundo lugar:
# [20, 50, "Curso", 'Python', 3.14]

lista = [20, 50, "Curso", 'Python', 3.14]

print("Lista original:",lista)

nombre = input("Ingresa tu nombre:")
lista[0] = nombre

edad = int(input("Ingresa tu edad:"))
lista[1] = edad

print("Lista modificada:",lista)