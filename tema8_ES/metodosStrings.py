import pprint

#Metodos de una cadena de texto
pprint.pprint(dir(''))

cadena = "en un lugar de la manchA"
#Pone la primera letra en Mayuscula y el resto en minuscula
print(cadena.capitalize())
#Cuenta el numero de letras. Ojo casesesitive
print(cadena.count('a'))
#Convierte cadena a minusculas y cuenta las letras a
print(cadena.lower().count('a'))

numero = '3'
print(numero.isdigit())
nuermo = 'a'
print(numero.isalnum())
print(numero.isalpha())

cadena = "     en un lugar de la manchA    "
print (cadena)
#Elimina todos los espacios / Espacios a la izq / Espacios a la der
print(cadena.strip())
print(cadena.lstrip())
print(cadena.rsplit())

#Convierte cadena en una lista de Strings
print (cadena.split())

#Empieza por ...
print(cadena.startswith("  "))