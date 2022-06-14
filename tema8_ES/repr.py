class Juguete:
    nombre = ""
    precio = 0.0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    # Sobreescribimos el metodo toString para devolver una cadena visible al usuario
    def __str__(self):
        return f'Mi nombre es {self.nombre} y mi precio es {self.precio}'


j1 = Juguete("Potato", 10.5)

print(str(j1))

print(repr(j1))
