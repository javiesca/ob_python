#Escribe una función que pueda decirte si un número (número entero) es primo o no.

def esPrimo(num):
    primo = False
    for i in range(2,num):
        if num % i == 0:
           primo = False
           break
        else:
            primo = True
    if primo == False:
        print("El número", num, "NO es primo")
    else:
        print("El número", num, "SI es primo")


    
esPrimo(12)
