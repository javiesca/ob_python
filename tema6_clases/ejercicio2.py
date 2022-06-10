
class Alumno():
    
    def __init__(self):
        self.nombre = ""
        self.nota = None

    def ponNota(self, nota):
        self.nota = nota
            
    def ponNombre(self, nombre):
        self.nombre = nombre

    def __str__(self):
        estado = ""
        if(self.nota >= 5):
            estado = "APROBADO"
        else:
            estado = "SUSPENSO"

        txt = "Nombre: {0} y tu calificacion es: {1}. Has {2}"
        return txt.format(self.nombre, self.nota, estado)
        

a = Alumno()
a.ponNombre("Javi")
a.ponNota(3)

print(a)