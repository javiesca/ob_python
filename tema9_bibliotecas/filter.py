numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def minFuncion(x):
    if str(x).startswith("pep"):
        return True

    return False

# Filter aplica una funcion a todos los elementos de una lista.
resultado = filter(minFuncion, ["pepe","pepito","juan"])

print(list(resultado))


