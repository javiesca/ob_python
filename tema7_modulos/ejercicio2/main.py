import time


def aCasa():
    hora = (int)(time.strftime('%H'))
    if hora >= 7 and hora < 19:
        print("Te quedan unas", 18 - hora, "horas para ir a casa")
    else:
        print("Es hora de irse a casa")
  

aCasa()