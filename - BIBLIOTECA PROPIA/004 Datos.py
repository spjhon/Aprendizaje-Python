# Para abrir un archivo y leer su contenido para luego ser procesado en python

archivo = open ("Prueba.txt", "r")

for linea in archivo:
    print (archivo)
    
archivo.close

# En las lineas de arriba se permite leer e imprimir desde un archivo de texto

#Para crear un archivo

---------------------------------

# Para crear un archivo se va a crear una lista para guardar los datos

datos = ["Cada elemento de la lista", "Es una linea", "Del archivo que se va a crear"]

# Lo que se hace con la w es que si no existe el archivo lo crea, luego lo que se hace es imprimir cada una de las lineas de la lista en el archivo
archivo_e = open ("Nombre_del_archivo_a_crear.txt", "w")

for i in datos:
    archivo_e.write (i + "\n")

archivo_e.close

------------------------------------------

# Ahora se le va a decir al usuario que ingrese la informacion y que quede almacenada en un documento

#Solicitar al usuario 2 datos que va a almacenar

print ("Digite los datos: ")

informacion = str(input())

#Ahora se va a cear un archivo

k = open ("informacion.txt", "w")

for i in informacion:
        k.write (i)

k.close

------------------------------------

# Crear un programa en python que permita lo siguiente:

# Solicitar al usuario un numero entero comprendido entre 1 - 10
# Realizar la tabla de multiplicar de ese numero ingresado por el usuario
# Los resutlados de esa tabla mostrarlos en un archivo de texto

a = int (input ("Ingrese el numero de la tabla: "))
b = 10
resultado = []
while b>0:
    print (a, "x", b, "=", str (a*b))
    n = a, "x", b, "=", str (a*b)
    b -= 1
    resultado.append (str(n))
    resultado.append ("\n")
while 1 > a > 10:
    print ("No es valido")
    a = int (input ("Ingrese el numero de la tabla: "))

k = open ("tabla_de_multiplicar.txt", "w")

for i in resultado:
    k.write (i)

k.close