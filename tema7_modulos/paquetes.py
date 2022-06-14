# Colección de modulos y paquetes

# Se importa nombreCarpeta.modulo
import paqueteOperaciones.suma

# Paquetes dentro de paquetes los llamamos de la maneta que queramos
import paqueteOperaciones.sumador.suma as SUM

import paqueteOperaciones.restador.resta as RES



def main():
    print(paqueteOperaciones.suma.suma(4,3)) #carpeta.modulo.funcion(valorA,valorB)

    #Instanciamos. Creamos objeto de la clase Multiplicador en el paqueteOperaciones
    mult = paqueteOperaciones.suma.Multiplicador()

    print(mult.multiplica(4,2)) #objeto creado arriba, funcion de esa clase, valores

    resta = paqueteOperaciones.restador.resta.resta(5,3)

    # Invocamos los paquetes y ejecutamos las funciones dentro de esos paquetes
    print(SUM.suma(1,3))
    print(RES.resta(2,1))



if __name__ == '__main__':
    main()