def esBisiesto(anio):
    bisiesto = False
    if (anio % 4 == 0) or (anio % 100 == 0 and anio % 400 == 0):
        bisiesto = True
    else:
        bisiesto = False

    if bisiesto == True:
        print("El año", anio, "es bisiesto")
    else:
        print("El año", anio, " NO es bisiesto")

esBisiesto(2005)