# Crear una funcion que pida dos numeros. 
# Si el primero es mayor al segundo, el programa debe retornar el valor 1; 
# si el segundo es mayor al primero, debe retornar -1; si ambos son iguales, debe retornar 0

def pedirNúmeros():
    num1 = float(input("Ingresa el primer número:"))
    num2 = float(input("Ingresa el segundo número:"))

    if num1 > num2:
        return 1
    elif num2 > num1:
        return -1
    else : 
        return 0

print(pedirNúmeros())