# Ejercicio 07. Hacer un programa que muestre todos los numeros impares entre
# dos numeros que elija el usuario

numeroinferior = int(input("Ingrese Limite Inferior: "))
numerosuperior = int(input("Ingrese Limite Superior: "))

if numeroinferior > numerosuperior:
    print ("El limite inferior es mayor que el limite superior, no se puede hacer la comparacion")
    exit()
else:
    print (f"Los numeros impares comprendidos en los limites {numeroinferior} y {numerosuperior} son:")
    if numeroinferior%2 != 0:
        while numeroinferior <= numerosuperior:
            print (numeroinferior)
            numeroinferior += 2
    else:
        numeroinferior += 1
        while numeroinferior <= numerosuperior:
            print (numeroinferior)
            numeroinferior += 2
            
# Otra forma de hacerlo utilizando el for

# Ejercicio 07. Hacer un programa que muestre todos los numeros impares entre
# dos numeros que elija el usuario

numero1 = int(input("Ingrese Limite Inferior: "))
numero2 = int(input("Ingrese Limite Superior: "))

if numero1 < numero2:
    for contador in range(numero1, (numero2 + 1)):
        if contador%2 == 1:
            print(contador)

# Otra forma mas de hacerlo con el for

numero1 = int(input("indique el primero numero: "))
numero2 = int(input("Indique el segundo numero: "))
     
if numero2 > numero1:
    for impar in range(numero1, (numero2 + 1)):
        if impar % 2 != 0:
            print(impar)
else:
    print("EL segundo numero debe ser mayo al primero")
