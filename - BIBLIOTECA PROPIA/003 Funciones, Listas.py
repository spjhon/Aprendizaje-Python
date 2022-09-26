# Como ejemplo se va a hacer una calculadora basica con funciones
# SUMA, RESTAR, MULTIPLICAR Y DIVIDIR
# Estas son las recomendaciones generales para iniciar un algoritmo con funciones
"""
1. IMPORTAR LAS LIBRERIAS A UTILIZAR
2. DECLARAR VARIABLES GLOBALES
3. DEFINIR FUNCIONES
4. CODIGO GENERAL
"""

# Vamos a importar una libreria con la
# palabra reservada import


import os # Importar la libreria del sistema operativo
os.system ("cls") # De esta forma utilizamos una opcion del sistema que se llama cls

# en este ejercicio no se declaran variables globales
# si se necesita se utiliza global
global g

def sumar (num1, num2): # Aqui solo se define la funcion
    resultado = num1 + num2
    return resultado

print ("Digite dos numeros para sumar: ")
a = float (input("Primer numero: "))
b = float (input("Segundo numero: "))

# Ahora vamos a llamar la funcion
print (f"La suma es: {sumar(a,b)}")

def dividir (num1,num2):
    if num2 == 0:
        print ("No se puede dividir entre 0")
    else:
        resultado = num1/num2
        return resultado
    
#Codigo general

#1. Importar las librerias a utilizar
import os # Importar la libreria del sistema operativo
os.system("cls")#CLS es acronimo de Clear Screen o limpiar pantalla
#2. Declarar variables globales
global g
#3. Definir funciones
#Función sumar
def sumar(num1, num2):
    resultado=num1+num2
    print("La suma es: ",resultado)
#Función restar
def restar(num1,num2):
    resultado=num1-num2
    print("La resta es: ",resultado)
#Función multiplicar
def multiplicar(num1,num2):
    resultado=num1*num2
    print("La multiplicación es: ",resultado)
#Función división
def dividir(num1,num2):
    if num2==0:
        print("No se puede dividir entre cero")
    else:
        resultado=num1/num2
        print("La división es: ",resultado)
#4. 
print("Elija una opción:")
print("1. Suma \n2. Resta \n3. Multiplicar \n4. Dividir")
opc = int(input())
if opc==1:
    print("Digite dos números")
    a=float(input())
    b=float(input())
    sumar(a,b)
elif opc==2:
    print("Digite dos números")
    a=float(input())
    b=float(input())
    restar(a,b)
elif opc==3:
    print("Digite dos números")
    a=float(input())
    b=float(input())
    multiplicar(a,b)
elif opc==4:
    print("Digite dos números")
    a=float(input())
    b=float(input())
    dividir(a,b)
else:
    print("La opción digitada es erronea.")
---------------------------------------    
#Arreglos unidimensionales
#Listas
#Tuplas
#Pilas, colas

#Listas son tipos de dato mutables

ejemplo = [] #Lista vacia, la lista lleva parentesis rectangular
numeros = [0, 45, 56, -76, 89]

print(numeros[3])

#Tuplas son inmutalbes, llevan parentesis circulares
h = (2,5,9,10,34)
print(h[2])

# Por supuesto no olvidar que las listas se pueden recorrer con los for

#Diccionarios {}
diccionario = {
    "Nombres" : "Edisson",
    "Edad" : 35
}

---------------------------------------

#Ejercicio que se encuentra en las diapositivas que pide un listado
#de supermercado

import os
os.system("cls")
dat1 = list()
dat2 = list()
totalarticulos = int()
totalcompras = float()

def caja (totalarticulos):
    lastp = int(0)
    pregunta = str("si")
    while True:
        if pregunta != "no" and pregunta != "si":
            print ("Ingese una opcion correcta") # Aqui lo que hago es meterlo en un ciclo que no sale hasta que se aprete la tecla que es
            print ("Tienes mas articulos para agregar?, escriba si o no:")
            pregunta = input()
            continue
        while True: # Aqui se testea el primer input
            cant_articulos = str(input("Cuantos productos desea ingresar al inventario?: "))
            test = int()
            try:
                test == int(cant_articulos)
            except:
                print ("Solo numeros enteros")
                continue
            else:
                cant_articulos = int(cant_articulos)
                break
        for i in range (lastp, cant_articulos+lastp):
            dat1.append(input(f"Ingrese el nombre del producto {i}: ")) # Aqui se acepta lo que entre
            while True: # Aqui se teste cada uno de los elemento ingresados a la lista
                dat2.append(input(f"Ingrese el precio del producto: "))
                testeo = float()
                try: 
                    testeo == float(dat2[i])
                except:
                    print ("Solo numeros")
                    dat2.pop()
                    continue
                else:
                    break
            lastp += 1
        totalarticulos += cant_articulos
        print ("Tienes mas articulos para agregar?, escriba si o no:")
        pregunta = input()
        if pregunta == "si" or pregunta == "Si" or pregunta == "SI":
            continue
        elif pregunta == "no":
            break
    return totalarticulos

b = caja(totalarticulos) # Aqui toco sacar en una variable a parte el resultado de la funcion
print (f"TOTAL DE ARTICULOS: {b}") # Debido a esto no se puede sacar variables de las fuciones, solo listas

for i in range (0, int(b)):
    print (f"Producto: {dat1[i]}, ${dat2[i]}") #Parece que las listas si se pueden sacar en bruto de las fuciones
    totalcompras += float(dat2[i])

print (f"TOTAL COMPRAS: ${totalcompras}")
--------------------------------------
"""
Actividad 2:  
Escribamos una función numAleatorio() que retorne un número aleatorio entre 100 y 130, excepto los números 110, 115 y 120.  
Adicionalmente, una función números que imprima diez números aleatorios (retornados por la función numAleatorio()) alternando par, impar, comenzando por par.
numeros()
"""
def numAleatrio():
    while True:
        import random
        numero = random.randint(1, 10)
        if numero == 9 or numero == 8 or numero == 2:
            print ("numero prohibido")
            continue
        else:
            print (numero)
            break

while True:
    otro = input("presione la tecla 'enter' para otro numero o 'e' para terminar el programa")
    if otro == "e" or otro == "E":
        exit()
    elif otro == "" or otro == "":
        numAleatrio()   
        continue
    else:
        #continue
------------------------------------------

# LISTAS

#Ejercicio de clase componente practico
#Usando el conocimiento de ciclos, crea una función números que tenga una lista con los números PARES del 1 al 10 y 
# usa un ciclo para que los imprima.
listado = list()

def listado2():
    listado.clear()
    for i in range (0, 12, 2):
        listado.append ([i])

def inpresion():
    if bool(listado) != False:
        print (listado)
    else:
        print ("Listado vacio")
        
while True:
    print ("Que desea hacer?: 1 para crear la lista, 2 para imprimirla, otro numero para salir: ")
    deseo = input()
    if deseo == "1":
        listado2()
        print ("La lista fue creada")
        continue
    elif deseo == "2":
        inpresion()
        continue
    else:
        print ("Selecciono salir")
        break     

--------------------------------

"""
Escribamos un programa que nos permita crear una lista de 6 números aleatorios entre 1 y 20 en Python, y creemos dos funciones que reciban la lista como parámetro de la siguiente forma:
•	mayor(x) - Una función que imprima el número mayor valor de una lista x
•	primos(x) - Una función que imprima los números de la lista que son números primos
"""

import random
listado = list()
for i in range(0, 6):
    listado.append (random.randint(1, 20))

def mayor():
    mayor = int(0)
    listacopia = list()
    listacopia = listado.copy()
    print (listacopia)
    while bool(listacopia) != False:
        print (listacopia)
        if mayor >= listacopia[0]:
            listacopia.pop(0)
        elif mayor < listacopia[0]:
            mayor = listacopia[0]
            listacopia.pop(0)
    print(f"El mayor es: {mayor}")
    return mayor


mayor()

def primos():
    listacopia = list()
    listacopia = listado.copy()
    print (listacopia)
    listPrimos = list()
    for i in range (0, 6):
        ran = int(listacopia[i])
        if ran > 1:
            for n in range (2, int(ran/2)+1):
                if (ran % n) == 0:
                    break
            else:
                listPrimos.append (ran)
                
    print ("Los primos son: ")
    print (listPrimos)
    return listPrimos

primos()

--------------------------

# Matrizes
#como declarar una matriz
matrizvacia = [[]]
datos = [[3,5,8], [4,6,7], [9,9,9]]
#Nemotecnia

#La forma de declarar las variables es variable = [][], de esta forma se sabe cantidad de filas y cnatidad de columnas
#EL ciclo for es el utilizado para recorrer las matrices, un for para la fila y el otro for para las columnas

# Ejemplo dado en las diapositivas

#Matríz
#Programa que crea una matríz y el usuario ingresa los datos
import os
os.system("cls")
filas=int(input("Digite el número de filas: "))
columnas=int(input("Digite el número de columnas: "))
matriz=[[]]

for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        valor=int(input("Fila {}, Columna {} :".format(i, j)))
        matriz[i].append(valor)

for i in range(filas):
    for j in range(columnas):
        print(matriz[i][j], end="")
    print("")


-------------------------

# Actividad 1:  Vamos a escribir una función que llene una matriz de 5 filas y 10 columnas 
# con números enteros entre 1 y 100 aleatorios, imprima los valores máximo y mínimo y sus 
# posiciones dentro de la matriz.

import random
columnas = int(10)
filas = int(5)
lista = list()
o = int(1)
matriz = []
mayor = int()
maximo = int(0)

for z in range (filas):
    for t in range (columnas):
        lista.append(random.randint(1, 100))
    matriz.append(lista)
    if maximo <= max(lista):
        maximo = max(lista)
    lista = list("")
    
for r in range (filas):
    for y in range (columnas):
        print (matriz[r][y], end = " ")
    print ("\n")

# print (f"Este es el punto fila 2, columna 3: {matriz[1][2]}")

print (f"El mayor numero de la matriz es: {maximo}")
