# Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, 
# y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

def calcularTotal():
    try:
        cantidad = float(input("Ingresa la cantidad :"))
        iva = input("Ingresa el IVA:").strip()

        if iva == "":
            iva = 0.21
        else:
            iva = int(iva)
            if iva < 0:        
        
                return "La cantidad de IVA es negativo. No podemos avanzar"
        
            iva = iva / 100        
        
        total = (cantidad * iva) + cantidad
        return total
    
    except ValueError:
        return "Error: Ingresa solo números"
    
print("El total de su monto es:",calcularTotal())