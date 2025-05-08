# No importa que lleve parentesis aun asi lo va a reconocer como tupla
tupla = (1, 2, 3, 4, 5)
tupla2 = (6, 7, 8, 9, 10)

print(tupla)
print(type(tupla))

print(tupla[2])
print(tupla[0:3])
print(tupla + tupla2)

# No se puede modificar sus datos dentro de una tupla
tupla[2] = 10
print(tupla)