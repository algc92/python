diccionario = {1 : 2, 2 : 3, 3 : 4}
diccionario2 = {4 : 5, 6 : 7}
print(diccionario,"\n")

# Elimina tomando como parametro una llave
diccionario.pop(3)
print(diccionario,"\n")

# Devolver el valor de una llave
print(diccionario.get(2),"\n")

# Añade un nuevo elemento al diccionario al final pasando llave y valor
diccionario.setdefault("Nombre", "Leonardo")
print(diccionario,"\n")

# Actualizar un valor ( Lo concatena ) y va a mantener una llave repetida
diccionario.update(diccionario2)
print(diccionario,"\n")

# Copiar el diccionario
diccionario.copy()
print(diccionario,"\n")

# Limpiar el diccionario
diccionario.clear()
print(diccionario,"\n")
