"""
Ejercicio 3.
Escribir un programa que muestre los cuadrados (un numero multiplicado por si mismo)
de los 60 primeros numeros naturales
resolverlo con el bucle for y el bucle while
"""
# con while
contador = int(0)
potencia = int(0)
while contador != 11:
    potencia = contador**2
    print (f"El cuadrado de {contador} es: {potencia}")
    contador += 1

#con for

contador = int(0)
potencia = int(0)

for contador in range(0, 10):
    potencia = contador**2
    print (f"El cuadrado de {contador} es: {potencia}")