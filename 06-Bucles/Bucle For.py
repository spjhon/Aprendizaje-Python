"""
# FOR, estructura iterativa que se repite

for variable in elemento_iterable (puede ser una lista, rango, tupla, etc)
    BLOQUE DE INSTRUCCIONES

El bloque de instrucciones se repetira hasta que se cumpla el elemento iterable
"""

# Ejemplo con un rango,
contador = 1
listado = list() # hay que inicialiar la variable en modo lista
print ("Se te pediran 5 numeros: ")
for contador in range(1, 6): # El for modifica el contador a medida que hace el ciclo, haciando que el contador al final sea otro
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