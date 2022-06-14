#Escritural

f = open('miFichero.txt', 'a')
f.write("datos\n")
f.write("datos2\n")
f.write("Ahora con 'a' -> append. Agregamos al final del archivo.\n")
lista = [
    'una linea\n',
    'dos lineas\n',
    'tres lineas'
]
f.writelines(lista)
f.close()

#Ejemplo de escreitura

def escribe(fichero, datos):
    f2 = open(fichero, 'w')

    for linea in datos:
        if not linea.endswith('\n') :
            linea = linea + '\n'

        f2.writelines(linea)

    f2.close()

lista2 = [
    'Javier',
    'Viesca\n',
    'Tuñón'
]

escribe('miFichero2.txt', lista2)