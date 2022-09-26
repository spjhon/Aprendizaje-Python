# LISTAS
# Son colecciones o conjuntos de datos/valores, bajo un unico nombre.
# Para acceder a esos valores podemos usar un indice numerico

pelicula = "Batman"

# Asi se define una lista
peliculas = ["Batman", "Spider-Man", "El Senor de los Anillos"]
cantantes = list(("2pac", "Drake", "Jenifer lopez")) # ESTO ES UNA TUPLA CONVERTIDO EN UNA LISTA
years = list(range(2020, 2050)) # asi se define una lista por medio de los rangos
variada = ["VICTOR", 30, 4.4, True, "Texto"]


# Cualquiera de los elementos son llamados indices

print (pelicula)
print (cantantes)
print (years)
print (variada)

# Como utilizar los indices de las diferentes listas

# Como acceder a los indices
print (peliculas[1])
print (peliculas[-2])

print (cantantes[1:3]) # de una parte a otra
print (peliculas[1:]) # de aqui en adelante

# hacer reemplazos en las listas
peliculas = ["Batman", "Spider-Man", "El Senor de los Anillos"]

pelicula = "otra cosa"
peliculas[1] = "Gran torino"
peliculas[2] = pelicula

print (peliculas)

# Anadir elementos a una lista

cantantes.append ("Kacey O")

print (cantantes)

#Recorrer lista

print ("LISTADO DE PELICULAS")

for b in peliculas: # Esto quiere decir mientras queden elementos en la lista, vaya iterando y ve guardando cada uno de los elementos en la variable pelicula
    print(b)
    print (f"{peliculas.index(b)}. {b}")