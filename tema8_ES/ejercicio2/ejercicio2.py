import pickle


class Juguete:
    nombre = ""
    modelo = ""
    precio = 0.0
    unidades = 100

    def __init__(self, nombre, modelo, precio):
        self.nombre = nombre
        self.modelo = modelo
        self.precio = precio
        self.unidades = self.unidades - 1

    def vender(self, unidades):
        self.unidades = unidades - 1

    def __str__(self):
        return f'Nombre:{self.nombre}\nModelo:{self.modelo}\nPrecio:{self.precio}\nUnidades:{self.unidades}'


j1 = Juguete("Coche", "Fiat", 25.5)


def escribeBin(archivo, objeto):
    f = open(archivo,'wb')
    pickle.dump(objeto,f)
    f.close()

def leeBin(archivo):
    f = open(archivo, 'rb')
    objeto = pickle.load(f)
    f.close()
    return objeto

escribeBin('juguete.bin', j1)

nombre = leeBin('juguete.bin')

print(nombre)