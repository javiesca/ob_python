
pais = str(input("Introduce una lista de paises separadas por comas: "))

listaPaises = pais.split(',')

listaPaises = sorted(set(listaPaises))
print(listaPaises)