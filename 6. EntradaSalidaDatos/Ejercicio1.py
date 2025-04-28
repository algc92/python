# Realizar un programa que haga el proceso de formula general para la resolución 
# de ecuaciones, sabiendo que la formula general es la que está 
# en la imagen, el usuario debe ingresar los valores de "a", "b" y "c" 
# el programa debe hacer el proceso para que al final muestre el mensaje:
# "La solución es: <solucion>"
# 3x^2-5x+2=0 x=1 x=2/3

from math import sqrt

a = int(input("Ingrese el valor de a:"))
b = int(input("Ingrese el valor de b:"))
c = int(input("Ingrese el valor de c:"))

x1 = 0
x2 = 0

if((b ** 2) - (4 * a * c)) < 0 : print("No se puede realizar")
else : 
    x1 = (-b + sqrt((b ** 2) - (4 * a * c))) / (2 * a)
    x2 = (-b - sqrt((b ** 2) - (4 * a * c))) / (2 * a)

    print("La solución es: \nx1=",x1, "\nx2=",x2)