#Declaracion de una lista simple
lista_diasDelMes=[31,28,31,30,31,30,31,31,30,31,30,31]

print (lista_diasDelMes)       #imprimir la lista completa
print (lista_diasDelMes[0])   #imprimir elemento 1
print (lista_diasDelMes[6])   #imprimir elemento 7
print (lista_diasDelMes[11])  #imprimir elemento 12


#Declaracion de listas anidadas

lista_numeros=[['cero', 0],['uno',1, 'UNO'], ['dos',2], ['tres', 3], ['cuatro',4], ['X',5]]

print (lista_numeros)      #imprimir lista completa

print (lista_numeros[0])    #imprime el elemento 0 de la lista
print (lista_numeros[1])    #imprime el elemento 1 de la lista

print (lista_numeros[2][0]) #imprime el primer elemento de la lista en la posicion 2
print (lista_numeros[2][1]) #imprime el segundo elemento de la lista en la posicion 2

print (lista_numeros[1][0])
print (lista_numeros[1][1])
print (lista_numeros[1][2])

#Cambiando el valor de uno de los elementos de la lista

lista_numeros[5][0] = "cinco"
print (lista_numeros[5])

input()
