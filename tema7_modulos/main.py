#Importamos el modulo operaciones.py y los llamamos ope
import operaciones as ope 
import math
import sys
import pprint

def main():
    # LLamo a las funciones suma y resta
    res = ope.suma(2,3)
    resResta = ope.resta(10,5)
    print("Hola en main()", res, resResta)
    print(ope.como_me_llamo())

    # LLamo a la clase en operador 
    op = ope.operador()
    print(op.multiplicacion(4,2))

    # Podemos llamar a variables
    print(ope.PI)

    

if __name__ == '__main__':
    main()

#Imprime los directorios
print(sys.path)

#Usando modulo 'PPRINT' -> Muestra de forma ordenada diccionarios y listas
pprint.pprint(sys.path)

