#COMPOSICION DE CLASES

class Motor:
    tipo = "diesel"

class Ventanas:
    cantidad = 5

    def cambiarCantidad(self, valor):
        self.cantidad = valor

class Ruedas:
    cantidad = 4

class Carroceria:
    ventanas = Ventanas()
    rudas = Ruedas()

class Coche:
    motor = Motor()
    carroceria = Carroceria()

c = Coche()

#Como herencia de clases pero instanciando con . 
print("Motor es", c.motor.tipo)
print("Ventanas: ", c.carroceria.ventanas.cantidad)

#Cambiamos cantidad de ventanas
c.carroceria.ventanas.cambiarCantidad(3)
print("Ventanas: ", c.carroceria.ventanas.cantidad)
