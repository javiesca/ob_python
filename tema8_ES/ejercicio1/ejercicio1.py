

def escribeCadena(archivo, cadena):
    f = open(archivo, 'w')
    f.write(cadena)
    f.close()

def leeCadena(archivo):
    l = open(archivo, 'r')
    cadena = l.read()
    l.close()
    print(cadena)

def main():
    escribeCadena('miArchivo.txt', "Ejercicio1. Escribir y leer archivos")
    leeCadena('miArchivo.txt')


if __name__ == '__main__':
    main()