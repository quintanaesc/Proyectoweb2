from random import randint

def imprime():
    nombre=str(input("¿Cual es tu nombre?: "))
    print(f"Tu nombre es {nombre}")

def suma():
    x=float(input("Ingresa un numero flotante: "))
    y=float(input("Ingresa otro numero flotante: "))
    print(f"El resultado de sumarlos es {x+y}")

def logicaInverso():
    x=bool(int(input("Ingresa True o False (1 = True/ 0 = False): ")))
    print(f"El inverso del valor ingresado es {not(x)}")    

def logicaBinaria():
    x=bool(input("Ingresa True o False (1 = True/ 0 = False): "))
    y=bool(input("Ingresa True o False (1 = True/ 0 = False): "))
    z=str(input("Ingresa una operacion logica binaria (and / or / xor): "))
    print(operaLog(x,y,z))

def operaLog(x, y,  z):
    if z=="and":
        return x and y
    if z=="or":
        return x or y
    if z=="xor":
        return (x and y) or ((not(x)) and (not(y)))

def secNum():
    for i in range(11):
        print(i)

def adivinaInador():##adivina el numero del 1 al 10
    x=randint(1,10)
    respuesta=0
    while(not(respuesta==x)):
        respuesta=int(input("¿En que numero del 1 al 10 estoy pensando?: "))
        if(x<respuesta):
            print("te pasaste intenta otra vez")
        elif(x>respuesta):
            print("muy bajo intenta otra vez")
    print("Correcto :)")

##main
seguir=True
while(seguir):
    x=int(input("¿Que codigo quiere probar? ingrese"+
    "\n 1  para  imprimir nombre"+
    "\n 2  para  realizar suma"+
    "\n 3  para  optener el  inverso"+
    "\n 4  para  realizar una operacion logica binaria"+
    "\n 5  para  imprimir del 1 al 10 "
    "\n 6 para adivinar un numero entre el 1 al 10\n "))
    if x==1:
        imprime()
    elif x==2:
        suma()
    elif x==3:
        logicaInverso()
    elif x==4:
        logicaBinaria()
    elif x==5:
        secNum()
    elif x==6:
        adivinaInador()
    seguir=bool(int(input("¿Desea provar otro codigo? (1 = si/ 0 = no): ")))