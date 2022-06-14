class Juguete:
    nombre = ""
    precio = 0.0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    # Sobreescribimos el metodo toString para devolver una cadena visible al usuario
    def __str__(self):
        return f'Mi nombre es {self.nombre} y mi precio es {self.precio}'

    def __repr__(self):
        return self.__str__()


j1 = Juguete("Potato", 10.5)
j2 = Juguete("Dino", 3.4)

#Salida informal
print(str(j1))
print(j2)
#Para salidas por depuración
print(repr(j1))
