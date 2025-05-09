# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

edad = int(input("Ingrese su edad:"))

contador = 1

while contador <= edad:
    print("Haz cumplido: {} años".format(contador))
    contador += 1
        