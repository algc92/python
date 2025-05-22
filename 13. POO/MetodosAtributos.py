class FabricaTelefonos():
    marca = "Samsung"
    color = "Negro"
    mram = 32
    almacenamiento = 128
    
    # todo método instancia debe contener el parametro self
    def llamar(self, mensaje):
        return mensaje

    def escucharMusica(self):
        print("Estas escuchando música")

telefono = FabricaTelefonos()
print(telefono.marca)
print(telefono.color)
print(telefono.mram)
print(telefono.almacenamiento)

# Aqui se esta mostrando el método y se pasa como parametro el mensaje
print(telefono.llamar("Hola desde el método"))
telefono.escucharMusica()

