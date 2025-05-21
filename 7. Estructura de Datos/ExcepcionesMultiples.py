while True:
    try:
        num1 = int(input("Ingresa un número:"))
        resultado = 100 / 1
        print(resultado)
        break
  #  except ZeroDivisionError:
  #      print("No se puede dividir entre cero")
    except KeyboardInterrupt:
        print("Has cancelado la ejecución")
        break