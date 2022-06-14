#Manipulaciones

# r: lectura -- Solo se puede leer
# a: append -- añade solo al final
# w: escritura -- lo sobreescribe
# x: create -- lo crea, python lo hace por defecto

# Variable f = open ('ruta')
f = open('/etc/passwd', 'r')
#Variable datos se guarda lo que se lee
datos = f.read(18)
#Cerramos el fichero
#Imprimimos
print(datos)

#Mientas la linea no este vacia lee linea a linea. imprime linea a linea
while datos != "":
    datos = f.readline()
    print(datos)

#Leer el fichero en una lista de
datos = f.readlines()
f.close()
print(datos)
