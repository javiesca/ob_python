#Funcion sin parametros. Tienen que ir antes la funcion 
def sinParametros():
    print ("Nombre")

sinParametros ()
#------------------------------------------------------------------------------------
#Funcion con parametros.
def conParametros(nombre):
    print("Hola", nombre)

conParametros ("Javier")
#------------------------------------------------------------------------------------
#Funciónes dentro de función
def matematicas(num1, num2):
    def suma(num1, num2):
        print (num1+ num2)
    def resta(num1,num2):
        print (num1-num2)

    suma(num1,num2)
    resta(num1,num2)

matematicas(9,8)
#------------------------------------------------------------------------------------
#Función con variables
tempAyer = 15.0
def conParametros(nombre):
    temp = 18.0
    print("Hola", nombre,". Hoy hace", temp,"grados. Ayer haciá",tempAyer,"grados.")
#------------# Las variables dentro de una función solo se pueden usar dentro de una función

conParametros ("Javier")

#Función con variables por defecto
def nombre(nombre = "Javi"):
    print ("Hola", nombre)

nombre()
nombre("Juan")
#-----------------------------
def suma(a= 1,b=3,c=2):
    print(a+b+c)

suma()
suma(2)
suma(2,4) #Por orden (a=2, b=4)
suma(b=5, c= 5) #Nombre de parametro y cambiamos

#FUNCION CON PARAMETROS variables
# *args convierte valores en una TUPLA
def suma(*args):
    resultado = 0
    for i in args:
        resultado += i
    print (resultado)

suma(4,9)
suma(4,7,3,6,8,3,1,6,5,3)

# **kwargs convierte valores en un DICCIONARIO (clave:valor)
def suma2(**kwargs):
    for key, value in kwargs.items():
        print(key,"=",value)

suma2(a="piso", b = "rojo")

#FUNCIONES RETORNO MULTIPLE
def resta(a,b):
    return a-b

resultado = resta(10,4)
print (resultado)

def operaciones(a,b):
    return a+b, a-b, a*b, a/b

res = operaciones(7,5)
print (res) #Convierte la variable res en una tubla con las operaciones del return de
print(res[2]) #Nos da la operacion de la posicion de la tuble 2 (el 3er valor)

#FUNCIONES ANONIMAS O LAMBDA
#sin parametros
anonima = lambda:(print("Hola"))
anonima()
#con parametros
anonima2 = lambda nombre, nombre2: print("Hola", nombre,". Adios",nombre2)
anonima2("Javier", "Pedro")
#no tienen return, solo indicamos la suma de los parametros
anonima3 = lambda a,b,c: a+b+c
print (anonima3(1,2,3))

#------MAS EJEMPLOS--------------------------------
def sumador(**kwargs):
    inicial = kwargs['inicial'] if 'inicial' in kwargs else 0 #Si no damos valor a 'inicial', 'inicial' vale 0
    final = kwargs['final'] if 'final' in kwargs else 0 #Si no damos valor a 'final', 'final' vale 0
    resultado = 0
    for i in range(inicial, final+1): #Suma los valores que hay entre inicial y final a la variable resultado
        resultado +=i
    return resultado

print(sumador(inicial=5, final =15))