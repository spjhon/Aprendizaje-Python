"""
Ejercicio 4.
Pedir dos numeros al usuario y hacer todas las operaciones basicas de una calculadora
"""

numero1 = float(input("Digite el primer numero: "))
numero2 = float(input("Digite el segundo numero: "))

print (f"La suma de ambos numeros es: {str(numero1+numero2)}")
print (f"La resta de ambos numeros es: {str(numero1-numero2)}")
print (f"La multiplicacion de ambos numeros es: {str(numero1*numero2)}")
if numero2 == 0:
    print ("0 no es un numerador correcto")
else:
    print (f"La division de ambos numeros es: {str(numero1/numero2)}")
