
class Alumno():

    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

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

        txt = "Nombre: {0} \nCalificacion: {1} \n{2}"
        return txt.format(self.nombre, self.nota, estado)
        

j = Alumno("Javi", 7)

print(j)

j.nombre = "María"
j.nota = 9

print(j)