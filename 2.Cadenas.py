#Inicializando cadenas
cadena1 = 'Hola '
cadena2 = "Mundo"
print(cadena1)
print(cadena2)
concat_cadenas = cadena1 + cadena2 #Concatenación de cadenas
print(concat_cadenas)

#Para concatenar un número y una cadena se debe usar la función str()
num_cadena = concat_cadenas +' '+ str(3)  #Se agrega una cadena vacía para agregar un espacio
print(num_cadena)

#El valor de la variable se va a imprimir en el lugar donde se encuentre {} en la cadena
num_cadena = "{} {} {}".format(cadena1, cadena2, 3)
print(num_cadena)

#Cuando se agrega un númmero dentro de {#}, el valor la variable que se encuentra en esa posición
#dentro de la función format(), será impreso.
num_cadena = "Cambiando el orden:  {1}  {2}  {0} #".format(cadena1, cadena2, 3)
print(num_cadena)
input()
