# IF

a = 4
b = 7

if a > b: 
    print ("A es mayor que B")
else:
    print ("B es mayor que A")

# Match (match en python)
valor = 4

match valor:
    case 1: print ("vale 1")
    case 2: print ("vale 2")
    case 3: print ("vale 3")
    case 4: print ("vale 4")


# BUCLES

# While
print()
print("BUCLE WHILE")
contador = 1

while contador <= 10:
    print("contador vale", contador)
    if contador % 2 == 0:
        print(contador, "es un número par")
    contador +=1

# For
print()
print("BUCLE FOR")
lista = ["Javi","Elena","York", "Gelu", "Eu"]
lista2 = ["Orsca", "Noelia", "Iván"]

for item in lista2:
   lista.append(item)

lista.sort()
print (lista)  

nombre = "Elena"
encontrado = False

for item in lista:
    if nombre == item:
        encontrado = True
    
if encontrado == True:
    print("El nombre esta en la lista")
else:
    print("El nombre no está en la lista")

# CON PASS PODEMOS DEJAR UN BUCLE O SENTENCIA SIN IMPLEMENTAR PARA PODER SEGUIR PROGRAMANDO
for item in lista2:
    pass 
