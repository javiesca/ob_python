#Clase Dino
class Dino:
    #con _ delante NO MODIFICAR
    _encendido = False

    #funcion Apaga
    def apaga(self):
        self._encendido = False
        print("Luz apagada")

    #funcion Enciende
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

#Clases estaticas. Sin instanciar la clase están en la misma area de memoria
class Estatica:
    numero = 1

    def incrementa():
        Estatica.numero+=1

Estatica.incrementa()
print(Estatica.numero)

Estatica.incrementa()
print(Estatica.numero)

