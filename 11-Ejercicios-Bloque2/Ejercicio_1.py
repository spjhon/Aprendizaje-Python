# Ejercicio 1. Hacer un programa que tenga una lista de 8 numeros enteros y haga lo siguiente:
# -  Recorrer la lista y mostrarla
# -  Ordernarla y mostrarla
# -  Hacer funcion que recorra listas de numeros y devuelva un string
# -  Mostrar su longitud
# -  Buscar algun elemento (que el usuario pida por teclado)

import random
#Crear una lista
numeros = [13, 64, 52, 73, 21, 7, 91, 63]

# Crear funcion que recorra la lista y devuelta un string

def mostrarLista (lista):
    resultado = ""
    
    for elemento in lista:
        resultado += "Elemento: " + str (elemento)
        resultado += "\n"
    return resultado
        
print (mostrarLista (numeros))
# Recorrer y mostrar
""""print ("###########Recorrer y mostrar#################")
for numero in numeros:
    print (numero)"""

# Ordenar y mostras

print ("########### Ordenar y mostrar #################")
numeros.sort()
print (mostrarLista(numeros))

# Mostrar su longitud

print ("########### Mostrar su longitud #################")
print (len(numeros))

# Busqueda en la lista

print ("########### Mostrar su longitud #################")
busqueda = int(input("Introduce el numero: "))

comprobar = isinstance (busqueda, int)

while not comprobar or busqueda <= 0:
    busqueda = int(input("Introduce el numero: "))
else:
    print (f"Has introducido el {busqueda}")

print (f"########### Buscar en la lista el numero {busqueda} #################")

search = numeros.index (busqueda)

print (f"El numero buscado existe en la lista, es el indice: {search}")

