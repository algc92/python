# Escribir una tupla que tenga las letras del alfabeto. 
# Luego, debes pedir al usuario un número, el que haya ingresado, es la letra que debe imprimir el programa

abecedario = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")

letra = int(input("Ingresa el número de letra a obtener:\n"))

print("La letra corresponediente es:",abecedario[letra-1])

