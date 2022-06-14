numero = 5
texto = "quijote"
otromas = 1.2

# VERSION VIEJA (Python 2.??) NO MIRAR

# Imprimir textos de forma antigua
# PLACEHOLDERS
# %d Digit-Numero
# %s String-texto
# %f float - Número decimal

print("El número es %d y el texto es %s y tiene %.2f" % (numero, texto, otromas))

# VERSION FORMAT Hasta la versión 3.6

# {} dentro irá la variable
# Si ponermos numeros dentro de las llaves {1}, pone el orden de la tupla
# Podemos poner un valor dentro de las llaves y en el format decir que ese valor es igual a la variable

print ("El número es {n1} y el texto es {t1} y tiene {om}"
       .format(n1=numero, t1=texto, om=otromas)
)

# MEDIANTE STRINGS
# f'  '--dentro de las llaves pueden ir las variables. Metodo mas nuevo y mas recomendado
print(f'El numero es {numero} y el texto es {texto.upper()} y tiene {otromas}')

#Podemos meter instanciar funciones dentro de las llaves del print. Ejemplo...
def suma(a,b):
    return a+b
print(f'La suma de los numeros a+b es {suma(5,5)}')

#Podemos convertir enteros a string y viceversa
num = 511
print (type(num))
numtxt = str(num)
print(type(numtxt))


