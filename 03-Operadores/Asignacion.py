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

# Operadores incremento y decremento
year = 2021
# Incremento
year = year + 1
print (year)
# Decremento
year = year - 1

# Como CHECKEAR si una variable es por ejemplo entero o no
x = 200
print(isinstance(x, int))