"""
Ejercicio 2.
Escribir un script que nos muestre por pantalla
todos los numeros pares del 1 al 120
"""

numero = int(0)

while numero != 120:
    if numero%2 == 0:
        print (numero)
        numero += 1
    else:
        numero += 1
        
# Asi lo hizo el profe

contador = 1

for contador in range (1, 121):
    if contador%2 == 0:
        print(contador)