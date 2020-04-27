op=0
PI=3.1416
def menu ():
    print("\nCalculadora de areas!!")
    print("\nSeleccione la figura\n")
    print("1.Triangulo\n2.Circulo\n3.Rectangulo\n4.Trapecio isoceles\n5.Salir")

def triangulo():
    b=int(input("Ingresa la base del triangulo: "))
    h=int(input("Ingresa la altura del triangulo: "))
    print("Area = "+str((b*h)/2))
    l=(b*h)**(1/2)
    print("Perimetro = "+str(b+2*l))

def rectangulo():
    b=int(input("Ingresa la base del rectangulo: "))
    h=int(input("Ingresa la altura del rectangulo: "))
    print("Area = "+str(b*h))
    print("Perimetro = "+str(b*2+h*2))

def circulo():
    r=int(input("Ingresa el radio de tu circulo: "))
    print("Area = "+str((r*r)*PI))
    print("Perimetro = "+str(PI*(r*2)))

def trapecio():
    bmay=int(input("Ingresa la base mayor del trapecio: "))
    bmen=int(input("Ingresa la base menor del trapecio: "))
    h=int(input("Ingresa la altura del trapecio: "))
    trapecioa=((bmay+bmen)*h)/2
    print("Area = "+str(trapecioa))
    x=(bmay-bmen)/2
    l=((x*x)+(h*h))**(1/2)
    print("Perimetro = "+str(bmay+bmen+2*l))

while(op!=5):
    menu()
    op = int(input())
    if(op==1):
        triangulo()
    elif(op==2):
        circulo()
    elif(op==3):
        rectangulo()
    elif(op==4):
        trapecio()
    elif(op==5):
        print("\nHasta la proxima!!")
    else:
        print("Elige una opcion valida")

input()
