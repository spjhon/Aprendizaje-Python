# CONDICONALES, condicional IF
"""
Condiconal if

SI se_cumple_esta_condicion:
    Ejecutar grupo de instrucciones
SI NO:
    Se ejecutan otro grupo de instrucciones

if condicion:
    instrucciones
else:
    otras instrucciones
"""
# Ejemplo 1
from calendar import different_locale


print ("##############EJEMPLO 1#############")

color = input("Adivina el color: ")

if color == "rojo":
    print("El color es ROJO")
else:
    print("Color incorrecto")

# OPERADORES DE COMPARACION
"""
!= differente
== Igual
< Menor que
> mayor que
<= menor o igual que
>= mayor o igual que
"""
year = 2020
year = int(input("En que year estamos?")) # Si no se delcara la variable automaticamente se toma como string al utilizar el input
if year >= 2021:
    print ("Estamos de 2021 en adelante")
else:
    print("Es un year anteior a 2021")