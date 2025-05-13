# Crear un programa que tenga una lista, luego crear una funcion con la cual se van a pedir numeros al usuario para agregar a la lista. 
# Debes crear una segunda funcion en donde se ordenen los numeros pares e impares dentro de dos listas nuevas

lista = []
num = 0

def pedirNumeros():
    i = 0
    while i <= 5:
        num = float(input("Ingresa un número:"))
        lista.append(num)
        i += 1
    print(lista,"\n")

pares = []
impares = []

def ordernar():
    lista.sort()
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    print("Números pares:",pares)
    print("Números impares:",impares)

pedirNumeros()
ordernar()