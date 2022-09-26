nada = None
cadena = "esta es una cadena de texto"
entero = 99
flotante = 6.3
booleano = True
lista = [10, 20, 30, 40, 50]
listaString = [30, "cuarenta", 50, "sesenta"]
tuplaNocambia = ("no", "cambia") # Es una lista de datos que no cambia
diccionario = {
    "nombre": "juan",
    "apellido": "Patino",
    "curso": "Master en Python"
} # Es un tipo de coleccion de datos que perimte tener dato y valor en un archivo json
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
 
#Ahora se va a mostar como cambiar el tipo de variable desde su definicion
texto = "Muestra de texto"
numerito = str(776)
print (texto + " " + numerito)
