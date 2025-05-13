def entero():
    print("Este es un dato entero:")
    return 10

print(entero())

def decimal():
    print("Este es un dato decimal:")
    return 5.5

print(decimal())

def frase():
    return "Mi nombre es Leonardo"

print(frase())

# Es posible que al retornar varios números y/o letras estos sean asignados a cada variable de acuerdo a la cantidad retornada
def asignacion():
    return 'a', 'b', 'c', 'd', 'f'

a, b, c, d, e = asignacion()
print(a)
print(b)
print(c)