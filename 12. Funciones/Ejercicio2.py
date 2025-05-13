# Escribir una función que reciba un número entero positivo y devuelva su factorial.

def factorial():
    num = int(input("Ingresa tu número entero y positivo:"))
    if num > 0:
        factorial = 1
        for i in range(1, num + 1):
            factorial = factorial * i
        print(factorial)
    else:
        print("El número es negativo y no se puede procesar")

factorial()


def factorial2():
    from math import factorial
    num2 = int(input("Ingresa tu número entero y positivo:"))
    if num2 > 0:
        print(factorial(num2))
    else:
        print("El número es negativo y no se puede procesar")

factorial2()