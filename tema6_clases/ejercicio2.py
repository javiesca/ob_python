
class Alumno():
    
    def __init__(self):
        self.nombre = ""
        self.nota = None

    def ponNota(self, nota):
        self.nota = nota
            
    def ponNombre(self, nombre):
        self.nombre = nombre

    def imprime(self):
        print("Tu nombre es: ", self.nombre)
        print("Tu nota de examen es: ", self.nota)
        if self.nota >= 5:
            print("Has aprobado")
        else:
            print("Has suspendo")



a = Alumno()
a.ponNombre("Javi")
a.ponNota(6)

a.imprime()