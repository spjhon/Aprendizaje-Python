"""
La idea es evitar el bucle infinito
# BUCLE WHILE
Es una estructura de control que itera o repite la ejecucion
de una serie de instrucciones tantas veces como sea necesario
hasta que deje de cumplirse la condicion

while condicion:
    bloque de instrucciones
    aqui siempre tiene que haber una actualizacion del contador
"""
# una forma de contar y mostrar los numeros del 1 al 100

contador = 1

while contador <= 100:
    print (f"Estoy en el numero: {contador}")
    contador += 1