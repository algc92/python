# Escribir un programa que solicite al usuario una vocal en minúscula, y
# otra en mayúscula. El programa debe realizar la conversión de las letras
# de forma inversa a las que se ingresaron y al final deben ser concatenadas.

vocal = input("Ingresa una vocal en MINÚSCULA: ")
consonante = input("Ingresa una consonante en MAYÚSCULA: ")

vocal = vocal.upper()
consonante = consonante.lower()

print("La consonante es: {} \nLa vocal es: {}".format(consonante,vocal))
