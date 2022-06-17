from functools import reduce

listaNumeros = [1,5,4,7,5,8,9,3,11,15,18]
print(f'La lista de todos los números es: {listaNumeros}')


def numerosImpares(x):
    if x % 2 != 0:
        return x

listaImpares = list(filter(numerosImpares,listaNumeros))

print(f'La lista con los numeros impares es: {listaImpares}')


def suma (a,b):
    return a+b

sumaImpares = reduce(suma, listaImpares)

print(f'La suma de la lista con los números impares es igual a {sumaImpares}')