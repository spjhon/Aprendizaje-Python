
#HAY 3 COSAS BASICAS PARA INTERACTUAR CON PYTHON
# - OPERADORES MATEMATICOS O ARITMETICOS (SABER CUALES SON LOS SIMBOLOS DE LAS OPERACIONES ARITMETICAS BASICAS)
# - OPERADORES DE COMPARACION O RELACIONALES (EL MAYOR QUE Y MENOR QUE Y SUS COMBINACIONES)
# - TIPOS DE VARIABLES (DECLARACIONES)
# - OPERADORES LOGICOS (LAS COMPUERTAS LOGICAS)
-------------------------------------------------------------------------------------------------------
# IMPRIMIR 
# Este es un ejemplo de como imprimir o mostrar en pantalla
print("##############")
print("Hola Mundo!, Prueba de ejcucion de Python")
--------
# De esta forma se pueden unir dos textos con print
texto1 = "Master"
texto2 = " en Python"

Texto_unido = texto1 + texto2
print(Texto_unido)  # Evitar utilizar mucho el + para unir texto, es mejor la concatenacion con f.
---------
import os # De esta forma se importa el CLS del sistema para limipiar pantalla, tambien se pueden utilizar vairables
os.system("CLS")
print("Digite su nombre")
nombre=input() # Con input se le pide datos al usuario
os.system("CLS") # Asi se limpia pantalla
print( nombre +" me la sopla")
-------------------------------------------------------------------------------------------------------
# COMENTARIOS
# Este es un comentario efectuado para fines de entender el codigo mejor y se utliza el #
print("Hola, estos son la seccion de comentarios yse utiliza la almuadilla #")
"""
Estos
son
print("comentarios")
multinivel
"""
print("comentarios")

-------------------------------------------------------------------------------------------------------

# ENTRADA DE DATOS
nombre = input("Cual es tu nombre?: ")
edad = input("Cual es tu edad?: ")

# SALIDA DE DATOS 
# todo los print son srt o string
# Asi que si hay que hacer operaciones hay que convertir los datos
print(f"Me alegro de conocerte {nombre}, \nveo que tienes la edad de {edad}")
print(f"Me alegro de conocerte {nombre}, \nveo que tienes la edad de {edad} \npero de acuerdo al tiempo chino, tu edad es de {int(edad) + 2}")

-------------------------------------------------------------------------------------------------------
# VARIABLES
"""
Una varible es un contenedor de informacion
que dentro guardara un dato, se pueden crear 
muchas variables y cada una contener un dato distinto.
"""
# Crear variables e imprimirlas
texto = "Máster en Python"
texto2 = "Por Udemy"
numero = 45
print(texto)
print(texto2)
print(numero)
# Cambio del contenido de las variables e imprimirlas
texto = "Cambio de texto"
texto2 = "Nuevo cambio de texto"
numero = 89.6
print(texto)
print(texto2)
print(numero)
---------
# Ahora se va mostrar la CONCATENACION
nombre = "Juan "
apellido = "Patino "
web = f" Esta en internet + {nombre}"

print(nombre + apellido + "--" + web)
print(f"Vamos a imprimir {nombre}, {web}, y el apellido {apellido}")

# Esta es otra forma de CONCATENAR
print("Hola este es mi nombre {} {} y esta es la web {}".format(nombre, apellido, web))

# O la forma sencilla, directamente las variables
print (nombre, apellido, web)
---------
#  TIPOS DE VARIABLES
# Aca se muestran los tipos de variables y un ejemplo de como idenfiticarlas
nada = None
cadena = "esta es una cadena de texto"
entero = 99
flotante = 6.3
booleano = True
lista = [10, 20, 30, 40, 50]
listaString = [30, "cuarenta", 50, "sesenta"]
tuplaNocambia = ("no", "cambia")
diccionario = {
    "nombre": "juan",
    "apellido": "Patino",
    "curso": "Master en Python"
}
rango = range(9)
dato_byte = b"esto se supone es un tipo de dato tipo BYTE"
#Mostrar que tipo de dato guarda una variable
print (f"tipo de dato en la variable nada es: {type(nada)}")
print (f"tipo de dato en la variable cadena es: {type(cadena)}")
print (f"tipo de dato en la variable entero es: {type(entero)}")
print (f"tipo de dato en la variable flotante (con decimales) es: {type(flotante)}")
print (f"tipo de dato en la variable booleano es: {type(booleano)}")
print (f"tipo de dato en la variable lista es: {type(lista)}")
print (f"tipo de dato en la variable listaString es: {type(listaString)}")
print (f"tipo de dato en la variable TuplaNoCambia es: {type(tuplaNocambia)}")
print (diccionario)
print (f"tipo de dato en la variable Diccionario es: {type(diccionario)}")
print (rango)
print (f"tipo de dato en la variable Rango es: {type(rango)}")
print (dato_byte)
print (f"tipo de dato en la variable Dato Byte es: {type(dato_byte)}")
---------
#Ahora se va a mostar como cambiar el tipo de variable desde su definicion
texto = "Muestra de texto"
numerito = str(776)
print (texto + " " + numerito)
---------
# Para que aparezcan las comillas en el string
# una forma es utilizando el \, otra forma es utilizando comillas simpes ''
print ("texto \"con comillas\" ")
print ("asi 'se utilizan comillas simples'")

# para meterle un SALTO DE LINEA o un ENTER se utiliza un \n
#para meterle una tabulacion se utiliza \t
print ("Esta es una linea \nEsta es otra linea")
print ("antes de tabulacion \tDespues de tabulacion")

# con \r reemplaza letra a letra lo que esta atras del simbolo con lo que esta delante
# del simbolo y lo que sobre se deja
print ("Esto no se deberia \r     ")
-------------------------------------------------------------------------------------------------------
# OPERADORES ARITMETICOS
numero1 = 77
numero2 = 44
# con el = se puede asignar variables, es asigancion no igual

resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
restooresiduo = numero1 % numero2 # lo que sobre de la division sale con este operador

print ("***********CALCULADORA***********")
print (f"La resta es: {resta}")
print (f"La suma es: {numero1 + numero2}") # De esta forma se puede sumar de una vez en la concatenacion
print (f"La multiplicacion es: ", multiplicacion)
print (f"La division es: {division}")
print (f"La resto o residuo es: {restooresiduo}")
---------
# Operadores de asignacion
# = el igual es el mas simples y solo relacion (crea asigancion)
edad = 55
print(edad)

# Otro asignador es += el cual le suma a la variable en cuestion
edad += 5
edad -= 5
print(edad)
# lo que equivale a 
edad = edad + 5
print(edad)
---------
# Operadores incremento y decremento
year = 2021
# Incremento
year = year + 1
print (year)
# Decremento
year = year - 1
---------
# Este es el ejemplo de una funcion cuadratica
a=2
b=3
c=4
x1=(-b+(b**2-(4*a*c))**(1/2))/(2*a)
x2=(-b-(b**2-(4*a*c))**(1/2))/(2*a)
print (x1)
print (x2)
z=2**4
print (z)
-------------------------------------------------------------------------------------------------------
# CONDICIONALES, aca se expresan en varios ejercicios la condicional solo si y la condicional con si y no

# CONDICONALES, condicional IF
"""
Condiconal if

SI se_cumple_esta_condicion:
    Ejecutar grupo de instrucciones
SI NO:
    Se ejecutan otro grupo de instrucciones

if condicion:
    instrucciones
else:
    otras instrucciones
"""
# Ejemplo 1
print ("##############EJEMPLO 1#############")

color = input("Adivina el color: ")

if color == "rojo":
    print("El color es ROJO")
else:
    print("Color incorrecto")
---------
# Si condicional simple, if

print ("Digite su edad: ")
edad = int(input())  # int es acronimo de integer o en espanol entero, solo recibe numero entero

if edad>=18:
    print("Usted es mayor de 18 anos")
    
print ("Fin del programa") # Aca se muestra la diferencia de cuando se utiliza el no, si no se cumple la condicion pues es como di la condicional no existiera y se continua con la ejecucion del programa
---------
# OPERADORES DE COMPARACION
"""
!= differente
== Igual
< Menor que
> mayor que
<= menor o igual que
>= mayor o igual que
"""
year = 2020
year = int(input("En que year estamos?")) # Si no se delcara la variable automaticamente se toma como string al utilizar el input
if year >= 2021:
    print ("Estamos de 2021 en adelante")
else:
    print("Es un year anteior a 2021")

---------
# Si condicional compuesto, if - else

print ("Digite su edad: ")
edad = int(input())                 

if edad>=18:
    print ("Usted es mayor de 18 anos")
else:
    print ("No es mayor de 18 anos")
    
print ("Fin del programa") 
---------
# Ejercicio utilizando los residuos de la division para determinar cuando un numero par o impar
# Residuo o modulo de la division % si el residuo de la division entre 2
# es 0 va a ser par
# Pero, sie l residuo de la division entre 2 es 1, es impar
#si se desea que no se ejecute una linea o lineas de codigo especificas se selecciona todo el codigo y se le ponen 3 comillas
# al principio y al final para anular el codigo.
# ojo, el simbolo = siginifica asignacion, cuando se realiza una comparacion se utiliza == para mirar si es igual y != para ver si es diferente

print ("Digite su edad: ")
variable = int(input())
variable = variable%2

if variable == 1 :
    print ("El numero es impar")
else:
    print ("el numero es par")
    
print ("Fin del programa")

#una forma mas rapida de escribirlo y validar si es 0
#el elif se utiliza para colocar otra condicional mas
numero = int(input("digite un numero: "))
if numero==0:
    print("el numero es cero, osea neutro")
elif numero%2==0:
    print("el numero es par")
else: 
    print ("el numero es impar")
---------
# Solicitar al usuario 2 numero y decir si el primer numero es mayor o menor.

numero01 = int(input("digite el primer numero: "))
numero02 = int(input("digite el segundo numero: "))

if numero01<numero02:
    print ("El primer numero es menor")
elif numero01>numero02:
    print ("El primer numero es mayor")
else:
    print ("Ambos numeros son iguales")
---------    
# disenar un programa que solicite un menu
#1. sumar dos numeros
#2. restar dos numeros
#3. multiplicar dos numeros
#4. dividir dos numeros, ojo, la division entre 0 no existe, el segundo numero digitado debe de ser diferente de 0

numero01 = int(input("digite el primer numero: "))
numero02 = int(input("digite el segundo numero: "))
print ("1. Sumar los numeros ingresados")
print ("2. Restar los  numeros ingresados")
print ("3. Multiplicar los numeros ingresados")
print ("4. Dividir los numeros ingresados")
desicion = int(input("que desea hacer? digite solamente 1,2,3 o 4: "))

if desicion == 1:
    resultado = numero01+numero02
    print ("El resutlado de la suma es ", resultado)
elif desicion == 2:
    resultado = numero01-numero02
    print ("El resutlado de la resta es ", resultado)
elif desicion == 3:
    resultado = numero01*numero02
    print ("El resutlado de la multiplicacion es ", resultado)
elif desicion == 4:
    if numero02 == 0:
        print ("No se puede dividir por 0")
    else:
        resultado = numero01/numero02
        print ("El resutlado de la division es ", resultado)
else:
    print ("No selecciono ninguna de las opciones")
---------
# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

print("Bienvenido a su Renta")
edad = int(input("favor digitar su edad  "))
ing = int(input("favor digitar tus ingresos mensuales  "))
if edad>= 16 and ing>= 1000 :
        print("estas obligado a tributar")
else :
    print("no estas obligado a tributar")
---------
# CONDICIONALES ANIDADAS Y MULTIPLES
#if multiple

# Se necesita que se indique que se soliite al usuario dos numeros y diga si es mayor menor o iguales
#Este codigo es del profesor
p=int(input("Digite el primer numero "))
q=int(input("Digite el segundo numero "))

if p==q:
    print ("Los numeros digitados son iguales")
elif p>q:                                           # este es multiple
    print ("El primer numero es mayor")
else:
    print("El primer numero es menor")
---------    
    
# Otro ejercicio, solicitar un numero al usuario y determinar si es positivo o negativo o es 0.
# los numeros mayores que 0 van a ser negativos y si son menores a 0 son negativos
    
numero = int (input("Digite el numero a evaluar"))

if numero == 0:
    print ("El numero es 0")
elif numero>0:
    print ("El numero es mayor a 0")
else:
    print ("El numero es menor 0")
---------    
    
#Ahora vamos a ver los anidados
#Programa que solicite al usuario su edad
#Si la edad es 18 o mas, solicite su sexo
#si el sexo es masculino, solicite su nombre
#Si el sexo es femenino solicite su apellido

edad = int (input("Digite su edad: "))

if edad >= 18:
    sexo = str (input("Digite su sexo, escribiendo M si es hombre o F si es mujer: "))
    if sexo == "M" or sexo == "m":          # El usuario puede meter mayuscula o minuscula
        nombre = str (input("Digite su Nombre: "))
    elif sexo == "f" or sexo == "F":
        apellido = str (input("Digite su Apellido: "))
    else:
        print ("Digito mal el sexo")
else:
    print("Usted no puede participar.")
---------    
# Los alumnos de un curso se han dividido en dos grupos 
# A y B de acuerdo al sexo y el nombre. El grupo A esta 
# formado por las mujeres con un nombre anterior a la M 
# y los hombres con un nombre posterior a la N y el grupo 
# B por el resto. Escribir un programa que pregunte al 
# usuario su nombre y sexo, y muestre por pantalla el grupo 
# que le corresponde.

inicial = str(input("Digite su inical: "))
sexo = str(input("Digite su sexo M para masculino, F para femenino: "))

if sexo == "F" or sexo == "f":
    if inicial == "a" or inicial == "A" or inicial == "B" or inicial == "b" or inicial == "c" or inicial == "C" or inicial == "D" or inicial == "d" or inicial == "E" or inicial == "e" or inicial == "F" or inicial == "f" or inicial == "G" or inicial == "g" or inicial == "H" or inicial == "I" or inicial == "i" or inicial == "j" or inicial == "J" or inicial == "k" or inicial == "K" or inicial == "l" or inicial == "L" or inicial == "m" or inicial == "M":
        print ("Pertenece al grupo A")
    else:
        print ("Pertenece al grupo B")
elif sexo == "M" or sexo == "m":
    if inicial == "N" or inicial == "n" or inicial == "o" or inicial == "O" or inicial == "P" or inicial == "p" or inicial == "Q" or inicial == "q" or inicial == "r" or inicial == "R" or inicial == "S" or inicial == "s" or inicial == "T" or inicial == "t" or inicial == "u" or inicial == "U" or inicial == "u" or inicial == "V" or inicial == "v" or inicial == "w" or inicial == "W" or inicial == "X" or inicial == "x" or inicial == "y" or inicial == "Y" or inicial == "z" or inicial == "Z":
        print ("Pertenece al grupo A")
    else:
        print ("Pertenece al grupo B")
else:
    print ("Pertenence al gurpo B")
    
# asi lo resolvio el profe

nombre=str(input("Digite su nombre: "))
sexo=str(input("Digite M si es masculino o F si es femenino"))

if sexo=="f" or sexo=="F":
    if nombre[0]<"m":
        print("Pertenece al grupo A")
    elif nombre[0]>="m":                # aca lo que se hace es tomar la primera letra del string y evaluarlo, python toma las letras como si fueran mayores o menoes de acuerdo al codigo ACII
        print("Pertenece al grupo B")
if sexo=="m" or sexo=="M":
    if nombre[0]>"n":
        print("Pertenece al grupo A")
    elif nombre[0]<="n":
        print("Pertenece al grupo B")
        
# otra forma de hacerlo

name = input ("Como te llamas?: ")
gender = input ("Cual es tu sexo?: ")

if gender == "M" or gender == "m":
    if name.lower() < "m": # no se alcanzo a copiar pero esta es una funcion que se puede utilizar tambien
        group = "A"
---------        
# Solucion del ejercicio que se encuentra en las diapositivas (mapa de xmind) que es
# una calculadora de indice de masa corporal

import os
os.system ("CLS")
print ("CALCULADORA DE MASA CORPORAL")
masa, altura = str(input("Ingrese peso en kilogramos: ")), str(input("Ingrese altura en metros: "))
masarevizada = masa.isdigit()   # con isdigit bota false o true si hay alguna letra (incluyendo los puntos decimales) en la cadena de caracteres no es un numero
alturarevizada = altura.replace(".", "", 1).isdigit()   # aca se utilizo el replace para eliminar 1 punto decimal y poder hacer la validacion y la conversion
if masarevizada == False or alturarevizada == False:
    print ("No se puede por que hay una o mas letras")
else:
    masafix = int(masa) #aca se transforma la varibble a una variable tipo int para que deje hacer la operacion
    alturafix = float(altura)
    imc = float(masafix/(alturafix**2))
    if masafix < 0 or alturafix < 0:
        print ("No se pueden meter numero negativos")
    else:
        if imc < 18.5 and imc >=0:
            mensajefinal = "Bajo de peso"
            print (f"Con un peso de {masa} y una altura de: {altura}, Su indice de masa corporal es: {imc}, lo que significa que: {mensajefinal}")
        elif imc >= 18.5 and imc < 25:
            mensajefinal = "Normal"
            print (f"Con un peso de {masa}kg y una altura de {altura}m, Su indice de masa corporal es: {imc}, lo que significa que: {mensajefinal}")
        elif imc >= 25 and imc < 30:
            mensajefinal = "Sobrepeso"
            print (f"Con un peso de {masa} y una altura de: {altura}, Su indice de masa corporal es: {imc}, lo que significa que: {mensajefinal}")
        elif imc >= 30:
            mensajefinal = "Obeso"
            print (f"Con un peso de {masa} y una altura de: {altura}, Su indice de masa corporal es: {imc}, lo que significa que: {mensajefinal}")
        else: 
            print ("Ingreso datos erroneos")
---------            
# este ejericico esta en las diapositivas el cual habla de que se pida tres numeros y mirar
# si dos son iguales o todos son diferentes


print ("VAMOS A EVALUAR 3 NUMEROS, POR FAVOR INGRESARLOS")
num1 = (input("Ingrese el primer numero: "))
num2 = (input("Ingrese el segundo numero: "))
num3 = (input("Ingrese el tercer numero: "))

# a,b,c=int(input()), int(input()), int(input()) de esta forma se puede declarar en una misma linea en python

if num1 == num2 == num3:
    print ("Los 3 numeros son iguales")
elif num1 == num2:
    print ("El primer y segundo numero son iguales")
elif num1 == num3:
    print ("El primer y tercer numero son iguales")
elif num2 == num3:
    print ("El segundo y tercer numero son iguales")
elif num1 != num2 != num3:
    print ("Ninguno de los numeros es igual")
else:
    print ("No ingreso un numero, verifique y vuelva a intentarlo")

# lo que me queda faltando es que si se mete algo diferente a un numero pues me muestre que
# no es un numero
# asi lo hizo el profe
print("Digita tres números enteros")
a,b,c=int(input()),int(input()),int(input())
if a==b and a==c and b==c:
  print("Los Números son iguales")
elif a!=b and a!=c and b!=c:
  print("Los números son diferentes")
else:
  print("Existen al menos dos número iguales")
---------

# otro ejercicio (el del ano biciesto)
print("Vamos a ver si es bisiesto o no")
ano = int(input("Ingrese la fecha a evaluar: "))

if ano % 4 != 0:
	print("No es bisiesto")
elif ano % 4 == 0 and ano % 100 != 0: 
	print("Es bisiesto")
elif ano % 4 == 0 and ano % 100 == 0 and ano % 400 != 0: 
	print("No es bisiesto")
elif ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
	print("Es bisiesto")
---------
