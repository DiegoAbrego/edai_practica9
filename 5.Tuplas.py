#Declaracion de una tupla
tupla_diasDelMes=(31,28,31,30,31,30,31,31,30,31,30,31)

lista_diasDelMes=[31,28,31,30,31,30,31,31,30,31,30,31]

print (tupla_diasDelMes)       #imprimir la tupla completa
print (tupla_diasDelMes[0])    #imprimir elemento 1
print (tupla_diasDelMes[3])    #imprimir elemento 4
print (tupla_diasDelMes[1])   #imprimir elemento 2

#Declaracion de tuplas anidadas

tupla_numeros=(('cero', 0),('uno',1, 'UNO'), ('dos',2), ('tres', 3), ('cuatro',4), ('X',5))

print (tupla_numeros)        #imprimir tupla completa

print (tupla_numeros[0])     #imprime el elemento 0 de la tupla
print (tupla_numeros[1])     #imprime el elemento 1 de la tupla

print (tupla_numeros[2][0])  #imprime el primer elemento de la tupla en la posicion 2
print (tupla_numeros[2][1])  #imprime el segundo elemento de la tupla en la posicion 2

print (tupla_numeros[1][0])
print (tupla_numeros[1][1])
print (tupla_numeros[1][2])
#Probando la mutabilidad de las listas vs la no mutabilidad de las tuplas
print("valor actual {}".format(lista_diasDelMes[0]))
lista_diasDelMes[0] = 50
print("valor cambiado {}".format(lista_diasDelMes[0]))
input()
#tupla_diasDelMes[0] = 50   #Esta asignación manda un error, ya que no se pueden cambiar los valores de las tuplas
