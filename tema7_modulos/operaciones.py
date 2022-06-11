# Módulo operaciones

PI = 3,14151921

def suma(a,b):
    return a+b
    

def resta(a,b):
    return a-b

def como_me_llamo():
    return __name__

class operador:
    def multiplicacion(self, a, b):
        return a*b


## Esto está en ambito global. NO SE SUELE HACER
print("Hola, soy el módulo de operaciones")