
# Ejecuta una funcion en todos los elementos de una lista
def cuadrado(x):
    return x * x

resultado = map(cuadrado, [1,2,3,4,5,6,7,8,9])

print (list(resultado))