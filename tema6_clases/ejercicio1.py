
#Creamos la clase Vehiculo
class Vehiculo():
       
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
    
    def print(self):
        print("Color: ", self.color, "\nNumero de ruedas: ", self.ruedas, "\nNumero de puuertas: ", self.puertas)

#Creamos la clase Coche que hereda de la clase Vehiculo
class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def print(self):
        print("Color: ", self.color, "\nNumero de ruedas: ", self.ruedas, "\nNumero de puuertas: ", self.puertas, "\nVelocidad: ", self.velocidad, "\nCilindrada: ", self.cilindrada)
        

#Creamos un objeto Coche y le damos valores a los atributos
c = Coche("Rojo", 4, 5, 120, 1900)
c.print()

