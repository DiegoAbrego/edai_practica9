#Las funciones pueden recibir n número de parámetros, no se necesita indicar el tipo
def imprime_nombre(nombre):
    print("hola "+nombre)  #Las cadenas se pueden concatenar con el +

#Llamada a la función
imprime_nombre("JJ")

#Definiendo una función que regresa el cuadrado de un número
def cuadrado(x):
    return x**2

x = 5
#La función format() sirve para convertir los parámetros que recibe, en cadenas; éstos valores son reemplazadas
#por las llaves de la cadena.
print("El cuadrado de {} es {}".format(x, cuadrado(x)))   #La función cuadrado() regresa un valor

#Definiendo una función que regrese más de un valor
def varios(x):
    return x**2, x**3, x**4

#Los valores que regresa la función pueden ser guardado en variables separadas por ,
val1, val2, val3 = varios(2)
print("{} {} {}".format(val1, val2, val3))

#Función con un parámetro con un valor por defecto
def cuadrado_default(x=3):
    return x**2

#Como la función tiene un valor por defailt, si se manda llamar la función sin especificar el parámetro, se toma el que
#tiene por defecto
cuadrado_default()

#La función regresa tres, valores, pero sólo nos interesa el primero y el tercero
val4, _, val5 = varios(2)
print("{} {}".format(val4, val5))

input()


#Variables Globales
#Se crea una variable en el espacio global de nombres
vg = 'Global'

#Se crea una función que imprime la variable global
def funcion_v1():
    print(vg)

#Llamada a la función que imprime la variable global
funcion_v1()

#Imprime la variable global
print(vg)

#Se crea una variable local que tiene el mismo nombre que la variable global
def funcion_v2():
    vg = "Local"
    print(vg)

#Llamada a la función
funcion_v2()  #Imprime valor local

#Imprime la variable global
print(vg)

#Se trata de imprimir el valor de la variable global, a diferencia de la función_v1(), se creó en el
#espacio local de la funcion_v3() una variable con el mismo nombre, por lo que se reemplaza la variable
#global
def funcion_v3():
    print(vg)
    vg = "Local"
    print(vg)

#Como se tiene una variable local y no se le ha asignado un valor, se genera un error
#funcion_v3()

#Para resolver el problema anterior y especificar que se quiere hacer uso de la variable global dentro de la
#función funcion_v4(), se tiene que agregar la palabra reservada global
def funcion_v4():
    global vg
    print(vg)
    vg = "Local"
    print(vg)

#Al momento de ejecutar la función se imprime el valor que tenía asignado vg antes de se modificado por la función.
#Después de asignar el valor, éste es impreso
funcion_v4()
#Se imprime la variable global con su valor modificado
print(vg)

input()
