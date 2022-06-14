#Clase Dino
from ast import Global


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

#Herencia
class Juguete:
    _encendido = True

    
    def enciende(self):
        self._encendido = True
    
    def apaga(self):
        self._encendido = False
    
    def isEncendido(self):
        return self._encendido

#Potato hereda metodos y atributos de Juguete
class Potato(Juguete):

    def quitarOreja(self):
        pass

    def ponerOreja(self):
        pass
#Dino hereda metodos y atributos de Juguete
class Dino(Potato, Juguete): #Por orden, primero hereda de Potato y Potato de Juguete

    def verEsquemas(self):
        pass

#Creamos instancia de Potato y encendemos y apagamos. Usamos metodos de clase padre Juguete
p = Potato()
p.enciende()
print (p.isEncendido())
p.apaga()
print (p.isEncendido())

#Creamos instancia de Dino y encendemos y apagamos. Usamos metodos de clase padre Juguete
d = Dino()
d.enciende()
print (d.isEncendido())

#Indice de metodos y atributos de una instancia de clase
print(dir(p))


#Constructor
class Alumno():
    edad = None
    nombre = None
    def __init__(self, nombre):
        self.edad = 17
        self.nombre = nombre

a = Alumno("Javi")
print("El alumno tiene ", a.edad, " años y se llama" ,a.nombre,".")

#Borra una instancia
del(a)


#Las clases son diccionarios en Python
_encendido = False

def enciende():
    print("Invoco a enciede")
    global _encendido
    _encendido = True

def apaga():
    global _encendido 
    _encendido = False

def isEncendido():
    return _encendido

diccionario = {
    '_encendido' : False,
    'enciende' : enciende,
    'apaga' : apaga
}

diccionario['enciende']()
diccionario['apaga']()
print(isEncendido())






