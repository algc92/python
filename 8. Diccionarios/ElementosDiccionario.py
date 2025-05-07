diccionario = {'Nombre' : "Leonardo", 'Apellido' : "Garcia", 'Estatura' : 175}

print("Diccionario original:",diccionario,"\n")
print("Llaves de diccionario:",diccionario.keys(),"\n")
print("Valores de diccionario:",diccionario.values(),"\n")

print("valor de clave:",diccionario["Estatura"],"\n")

#añadir un nuevo valor
diccionario["Peso"] = "58 kg"

print("Diccionario nuevo:",diccionario,"\n")

#modificar un valor
diccionario["Nombre"] = "Andres"

print("Diccionario nuevo:",diccionario,"\n")