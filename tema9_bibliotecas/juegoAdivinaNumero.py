
secreto = 50

valor = 0

while valor != secreto:
    valor = input("Introduce un número: ")
    valor = int(valor) # Convierte un str en un valor

    if valor > secreto:
        print("Te has pasado")
    elif valor < secreto:
        print("Mas alto")
    else:
        print("ACERTASTE!!!")


