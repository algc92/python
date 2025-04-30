# Crear un programa que pida al usuario una letra, y si es vocal, muestre
# el mensaje "Es vocal", Si no decirle al usuario que no es vocal

letra = input("Ingresa una letra:")

if letra.lower() in "aeiou":
    print("Es vocal")
else :
    print("No es vocal")
    