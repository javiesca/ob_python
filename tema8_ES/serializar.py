#Modulo pickel para convertir objetos en datos
import pickle

class Juguete:

    nombre = " "
    precio = 0.0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def getNombre(self):
        return self.nombre


j = Juguete("Potato", 10.4)
print(type(j))
print(j.getNombre())

#Serializar
f = open('datos.bin', 'wb')
#pickel.dump(objeto, f)
pickle.dump(j, f)
f.close()

fl=open('datos.bin', 'rb')
potato = pickle.load(fl)

print(type(potato))
print("Nombre: ",potato.getNombre(), "precio: ", potato.precio)

