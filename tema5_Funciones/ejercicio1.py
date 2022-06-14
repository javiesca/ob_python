
#Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.


def areaTriangulo(base, altura):
    return (base*altura)/2

def areaCuadrado(lado):
    return lado*lado 


areaT = areaTriangulo(4,6)
print("El area del triangulo es: ", areaT)

areaC = areaCuadrado(4)
print("El area del cuadrado es: ",areaC)