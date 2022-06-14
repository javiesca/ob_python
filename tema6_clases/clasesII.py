#Clases Abstractas

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass
    def diHola(self):
        print("Hola")

##NO SE PUEDEN INSTANCIAR LAS CLASES ABSTRACTAS
# a = Animal()

## Las clases que derivan de la clase abstracta TIENEN que implemetar sus metodos
class Perro(Animal):
    def sonido(self): ##OBLIGATORIO
        print("Guau")

class Gato(Animal):
    def sonido(self): ##OBLIGATORIO
        print("Miau")

p = Perro()
p.sonido() 
p.diHola()

g = Gato()
g.sonido()
g.diHola()

