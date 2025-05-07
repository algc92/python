# En el siguiente diccionario se encuentran capitales de los paises en el mundo, 
# debes realizar un programa que pida un pais al usuario, y muestre la capital de ese pais, 
# en dado caso el pais no este en el diccionario, se debe mostrar un mensaje diciendo que ese pais no se encuentra.
# {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", 
# "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

diccionario = {
               "Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", 
               "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose",
               "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", 
               "Venezuela": "Caracas", "España": "Madrid"
               }

pais = input("Ingresa un pais para conocer su capital:")

# Forma de validar si se encuentra dentro de un diccionario "in"
pais_formateado = pais.strip().title() # Elimina espacios al inicio/final y pone mayúsculas iniciales

if pais_formateado in diccionario:
    print(diccionario[pais_formateado])
else:
    print("El pais no se encuentra en el diccionario")