#Hacer un programa que pida al usuario su nombre, su edad y su sexo y los muestre de la siguiente forma:

#Te llamas: <nombre>

#Tu edad es: <edad>

#Eres: <sexo>

nombre = input("Ingrese su nombre:")
edad = int(input("Ingrese su edad:"))
sexo = input("Ingrese su sexo:")

print("Te llamas: {} \n Tu edad es: {} \n Eres: {}".format(nombre,edad,sexo))