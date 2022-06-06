#Clase Dino
class Dino:
    #con _ delante NO MODIFICAR
    _encendido = False

    def apaga(self):
        self._encendido = False
        print("Luz apagada")
    
    def enciende(self):
        self._encendido = True
        print("Luz Encendida")

#Instanciando la clase Dino
d = Dino()

#Ahora se puede acceder a la funcion o parametro dentro de la clase.
print(d._encendido)

#Se puede modificar desde fuera de la clase 
d._encendido = True
print (d._encendido)

d.apaga()
print(d._encendido)

d.enciende()
print(d._encendido)