# Escribir un programa que anada valores a una lista mientras que su longitud sea menor a 12
# Mostrar la lista

import random

lista = list(' ')*10

for elemento in range(0, len(lista)):
    x = int(random.randint(1, 100))
    lista.pop(elemento)
    lista.insert(elemento, str(x))
    print (lista) 
    
------------------------------------------

# Escribir un programa que anada valores a una lista mientras que su longitud sea menor a 12
# Mostrar la lista

contador = 0
lista = list()
while contador < 12:
    x = input("Inserte un numero a agregar a la lista: ")
    lista.append(x)
    contador += 1
    print (contador)
print (lista)

--------------------------------------------

# Asi lo hizo el profe

