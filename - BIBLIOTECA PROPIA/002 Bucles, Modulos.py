# La condicion while es que mientras se cumpla el while se ejecutan las acciones
#Aqui vamosa mostrar los numeros del 0 al 15
a = 1
while a <= 15:
    print ("Edisson Caicedo")
    print
    a = a + 1 #Otra forma de dicrlo es a += 1
-----------------------
# Imprimir en pantalla la tabla de multiplicar de un numero dado por el usuario

numero = float(input("Ingrese el numero para generar su respectiva tabla: "))
limite = int(input("Hasta donde quiere la tabla?: "))
multiplicador = int(0)

while multiplicador <= limite:
    
    print (f"{numero} x {multiplicador} = ", numero * multiplicador)
    multiplicador += 1

print ("\n")
print ("Fin de la tabla")

# otra forma de imprimir la tabla de multiplicar utilizando el ciclo for
# Otro ejemplo con el bucle for con tablas de multiplicar

print ("#################TABAL DE MULTIPLICAR##################")

numero_usuario = int(input("De que numero quieres la tabla?: "))
limite = int(input("Hasta donde quiere la tabla?: "))
limite += 1 # esto es por que el rango empieza desde 0 y la tabla del 6 iria hasta el 5 por ejemplo

if numero_usuario < 1 or limite < 1:
    print ("Numero incorrecto")
else:
    print (f"TABLA DE MULTIPLICAR DEL NUMERO {numero_usuario}")
    for numero_tabla in range(0, limite): # Aqui se le puede dar al rango un limite ingresado por el usuario
        print (f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
    else:
        print ("Fin de la tabla")
-----------------------

# Leer los numeros enteros del teclado, hasta que el usuario ingrese el 0,
# Finalmente, mostrar la sumatoria de los numeros ingresados

numero = int(input("Ingrese los numeros a sumar uno por uno (con 0 se acaba y muestra la sumatoria): "))
sumatoria = int(0)

while numero != 0:
    sumatoria += numero
    numero = int(input("Ingrese otro numero pal bulto (con 0 se acaba e imprime resultado): "))

print (f"La suma de todos los numeros que ingreso es: {sumatoria}")

-----------------

# Leer numeros de teclado, hasta que el usuario
# ingrese el 0. Finalmente, mostrar la sumatoria de todos los numeros positivos ingresados

numero = int(1)
sumatoria = int(0)

while numero != 0:
    numero = int(input("Ingrese otro numero pal bulto (con 0 se acaba e imprime resultado): "))
    if numero > 0:
        sumatoria += numero

print (f"La suma de todos los numeros POSITIVOS que ingreso es: {sumatoria}")

------------------
"""
# FOR, estructura iterativa que se repite

for variable in elemento_iterable (puede ser una lista, rango, tupla, etc)
    BLOQUE DE INSTRUCCIONES

El bloque de instrucciones se repetira hasta que se cumpla el elemento iterable
"""
# Explicacion del for desde misiontic, solamente indicando un numero de repeticiones

for gato in range(4):
    print ("prueba")

# Otra forma de utilizar el for, con un punto de partida y un punto final

for gato in range(0, 4):
    print ("prueba")
    print(gato)

# El tercer parametro que se le puede deifinir es el incremento, por defecto es 1
# Aqui se ven los numero pares del rango
for gato in range(0, 4, 2):
    print ("prueba")
    print(gato)

# Otra forma de utilizar el ciclo for
# Aqui se explican las tuplas

t=1, # Esta es una tupla ya que solo tiene un valor aunque este puede ser cambiado
t=[1,5,6,7,2] # Esta es una lista o en otros lenguages es un vector

# La otra opcion es utilizar la lista en el rango
# de esta forma se le dice al for que recorra la lista utilizando el rango
for i in t:
    print(i)

--------------------------

# Ejemplo con un rango,
contador = 1
listado = list() # hay que inicialiar la variable en modo lista
print ("Se te pediran 5 numeros: ")
for contador in range(1, 6):
    print ("Vor por el " + str(contador))
    listado.append (input("Ingrese un numero: ")) # append (adjuntar) es una funcion, de esta forma de agregan items al listado uno a uno cada vez que se ejecute la linea

print (f"Los numeros que fueron ingresados son: {listado}")

# Otro ejemplo con el bucle for con tablas de multiplicar

print ("#################TABAL DE MULTIPLICAR##################")

numero_usuario = int(input("De que numero quieres la tabla?: "))
limite = int(input("Hasta donde quiere la tabla?: "))
limite += 1 # esto es por que el rango empieza desde 0 y la tabla del 6 iria hasta el 5 por ejemplo

if numero_usuario < 1 or limite < 1:
    print ("Numero incorrecto")
else:
    print (f"TABLA DE MULTIPLICAR DEL NUMERO {numero_usuario}")
    for numero_tabla in range(0, limite): # Aqui se le puede dar al rango un limite ingresado por el usuario
        print (f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
    else:
        print ("Fin de la tabla")
        
---------------------------
        
# El mismo ejercicio de las tablas de multiplicar
# pero utilizando el ciclo for

print ("Digite un numero")
n = int(input())

for i in range (1, 11, 1):
    #res=n*i
    print (n, " x ", i, " = ", n*i)
    
---------------------------

# imprima los numeros del 1 al 10 al revez, utilizando el ciclo for
# como se puede observar no hay necesidad de inicializar la variable
for i in range (1, 11, 1):
    print (11-i)
    
# Tambien se pueden tener rangos al revez


---------------------------------
#Realizar un algoritmo que nos calcule la serie de Finonacci.
#La serie o secuencia de Fibonacci comienza con los numeros 0 y 1 y 1,
#y a partir de alli es posible calcular el siguiente valor como la suma 
# de los dos valores anteriores

#Por ejemplo, 1+1=2, 1+2=3, 2+3=5, etc.

#Asi, los primeros numeros de la secuencia son:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,.....

#Creemos un programa que a partir de un numero N ingresado,
#imprima los primeros N numeros de la serie de Fibonacci.

n = int (input("Ingrese un numero para mostrar su secuencia fibonacci "))
i = int (input("Ingrese desde donde desea inicar la secuencia: "))
fibo = int (1)
x1 = int(1)
x2 = int(1)
print ("0")
for i in range(1, n):
    fibo = x1 + x2
    print (fibo)
    x1 = x2
    x2 = fibo

    
# Program to display the Fibonacci sequence up to n-th term
# Otra forma de hacerlo
nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
       
# Otra forma mas de hacerlo
x,y=0,1

while y<50:
    print(y)
    x,y = y,x+y
    
# Una forma de ver los numeros fibonacci entre dos numeros enteros con la formula
# que dicta como se pueden determinar si un numero es fibonacci o no.
#fibonacci untill a number
import math
a = int(input('Enter a positive integer'))
z = int(input('Enter termination number'))

while a < z:
    a = a
    z = z
    b = ((5 * a * a) + 4)
    c = ((5 * a * a) - 4)
    d = math.sqrt(b)
    e = math.sqrt(c)

    if d % 1 == 0 or e % 1 == 0:
        print(str(a))
    a = a + 1

-----------------------

# Ejercicio. 
# Escribe el codigo usando break que reciba una palabra e imprima
#el numero de letras que tiene y las letras hasta que, o bien termine la palbra o encuentre
# la letra a.

cuentaletras = int(0)
n = str(input("Ingrese una palabra: "))
cuentaletras = len(n)
lista = list(n)

for i in range(0, cuentaletras):
    control = lista[i]
    if control != "a":
        print (lista[i])
    else:
        print ("Una 'a' fue encontrada")
        break

---------------------------------

# Ejercicio.
# Escribe un algoritmo que lea 10 numero e imprima cuantos
# son positivos, cuantos negativos y cuantos neutros (0)
# ACUERSEDE QUE EXISTEN LOS COMPARADORES LOGICOS IS y IS NOT

print ("A continuacion se van a solicitar 5 numeros: ")
mensaje  = ("primer,segundo,tercero,cuarto,quinto") #Aqui guardamos un mensaje que mas adelante se va a dividir e incrustar en una lista
numeros = list() #Aqui se van a guardar los numeros ingresados por el usuario
list = mensaje.split(",")
negativo = int()
positivo = int()
neutro = int()
for i in range (0, 5):
    numeros.append (input(f"Ingrese el {list[i]} numero de la lista de 5: "))
    try:
        int(numeros[i])
    except ValueError:
        print ("No se puede por que hay una o mas letras")
        exit()

for z in range(0, 5):
    if int (numeros[z]) < 0:
        print (f"El numero {numeros[z]} es negativo")
        negativo += 1
    elif numeros[z] == 0:
        print (f"El numero {numeros[z]} es neutro")
        neutro += 1
    else:
        print (f"El numero {numeros[z]} es positivo")
        positivo += 1

print (f"Con un total de 5 numeros, hubieron {negativo} negativos, {neutro} neutros y {positivo} positivos")

---------------------------------
# CONTINUE: When the program execution reaches a continue statement, the program execution immediately jumps back to the start of the loop.
# Loop tipo password
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
-------------------------------------
# Otra forma de pedir password en un solo paso
from ast import Not

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    if Not:
        break
print('Access granted.')

-----------------------------------
# Otra forma
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    if name == "Joe":
        break
print('Access granted.')

-----------------------------------

#importando modulos del sistema desde tiempo hasta random
# Ejemplo de random
import random
for i in range(5):
    print(random.randint(1, 10))

# Esta es otra forma
import random, sys, os, math

#Esta es otra forma
from random import *
-------------------
# Otra forma de pedir ciclos


while True:
    a = input("Ingrese numero: ")
    b = float()
    try:
        b = float(a)
    except:
        print ("Solo numeros")
        continue
    else:
        print ("Todo salio bien")
        break

print ("Fin del programa")