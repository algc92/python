# Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero

numero = int(input("Ingrese el número para obtener la tabla de multiplicar:\n"))

i = 1

print("Tabla del {}".format(numero)+"\n")

while i <= 10:
    print("{} x {} = {}".format(numero,i,numero*i))
    i += 1
