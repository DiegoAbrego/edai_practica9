#Se debe importat la librería para hacer uso de namedtuple
from collections import namedtuple

#Se crea la tupla con nombre
#El primer argumento es el nombre de la tupla, mientras que el segundo argumento son los campos
#p es la referencia a la tupla
planeta = namedtuple('planeta', ['nombre', 'numero'])

#Se crea el planeta 1 y se agregan a la tupla los valores correspondientes a los campos
planeta1 = planeta('Mercurio', 1)
print(planeta1)

#Se crea el planeta 2
planeta2 = planeta('Venus', 2)

#Se imprimen los valores de los campos
#Usando la referencia se llama a cada uno de sus campos
print(planeta1.nombre, planeta1.numero)
#Se obtienen los valores por el orden de los campos
print(planeta2[0], planeta2[1])

print('Campos de la tupla: {}'.format(planeta1._fields))
#Al igual que las tuplas, éstas no son mutables, si se trata de cambiar el contenido, se genera un error
#planeta1.nombre = 'Tierra'
input()
