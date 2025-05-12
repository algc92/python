# Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario dos numeros y mostrar el rango de numeros entre ambas cifras

for i in range(1, 11):
    print("Rango de número:",i)

print("\n")

numero1 = int(input("Ingresa el número inicial para el rango:"))

numero2 = int(input("Ingresa el número final para el rango:"))

print("\n")

for i in range(numero1, numero2 + 1):
    
    print(i)

    if i == numero2:
        break