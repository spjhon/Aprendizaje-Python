# Ejercicio 09. Un programa que nos pida un numero indefinidamente
#hasta que el usuario meta 1111 y vaya mostrando los numeros

contador = 1
while contador < 100:
    numero = int(input("Introduce un numero: "))
    
    if numero == 111:
        break
    else:
        print (f"haz introducido el {numero}")

