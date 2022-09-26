cantantes = ["2pac", "Drake", "Bad Bunny", "Julio Iglesias"]
numeros = [1,2,5,8,3,4,8]

# Los metodos para las listas son formas de procesar y manipulas las listas

print (numeros) # Aqui hace ordemaniento de numeros
numeros.sort()
print(numeros)

# Anadir elementos
cantantes.append("Natos y Waor")
cantantes.insert(1, "") # Este sirve pero se tiene que agregar en donde se debe de agregar o bota error, ojo que no reemplaza, inserta

# Eliminar elementos
cantantes.pop(1)
print (cantantes)

# Eliminar por el nombre en concreto, lo busca y lo elimina
cantantes.remove("Bad Bunny")

# Dar la vuelta, poner el ultimo elemento de primero y viceversa
numeros.reverse()

# Contar el numero de elementos y buscar dentro de una lista

print ("Drake" in cantantes) #Esto es un buscador lo que devuelve es un True si la encuentra o un False si no

# Contar elementos

print (len(cantantes))

# Cuantas vecesa aparece un elemento en una lista
print (numeros.count(8))

# Conseguir un indice
print (cantantes.index("Drake"))

# Unir dos listas
cantantes.extend(numeros)
print (cantantes)