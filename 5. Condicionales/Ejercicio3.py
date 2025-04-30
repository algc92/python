# Escribe un programa que pida dos palabras y diga si riman o no. 
# Si coinciden las tres últimas letras tiene que decir que riman. 
# Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.

palabra1 = input("Ingresa primer palabra: ")
palabra2 = input("Ingresa segunda palabra: ")

if len(palabra1) < 3 or len(palabra2) < 3:

    print("No se puede comparar")

elif palabra1[-3: ] == palabra2[-3: ]:
        print("Si riman")
elif palabra1[-3: ] == palabra2[-3: ]:
       print("Riman un poco")
else : 
        print("No riman")