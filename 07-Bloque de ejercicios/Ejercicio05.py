"""
Ejercicio 5.
Hacer un programa que muestre todos los numeros entre
dos numeros que diga el usuario.
"""
numero1 = str(input("Ingrese el primer numero: "))
numero2 = str(input("Ingrese el segundo numero: "))
contador = len(numero1) # Esta es una funcion que se utiliza para contar la cantidad de caracteres en un string
contador2 = len(numero2) # Esta es una funcion que se utiliza para contar la cantidad de caracteres en un string
control = str()
control2 = str()

if contador == 2: # Preguntando si la cadena de string tiene 2 caracteres
    string_list = list(numero1) # Si es positivo, numero1 se convierte en lista y se guarda en la variable string_list
    control = string_list[1] # Aqui se guarda en la variable control la posicion 1 (0,1) osea la posicion 2 de la lista
    if control == "-": # Preguntando si en esa variable se encuentra ese caracter en especifico
        print ("No se puede por que hay una o mas letras")
        exit() # Si se llega hasta aca se termina el programa

if contador2 == 2:
    string_list2 = list(numero2)
    control2 = string_list2[1]
    if control2 == "-":
        print ("No se puede por que hay una o mas letras")
        exit()


numero1revizado = numero1.replace("-", "", 1).isdigit()   # con isdigit bota false o true si hay alguna letra (incluyendo los puntos decimales) en la cadena de caracteres no es un numero
numero2revizado = numero2.replace("-", "", 1).isdigit()   # aca se utilizo el replace para eliminar 1 punto decimal y poder hacer la validacion y la conversion
if numero1revizado == False or numero2revizado == False:
    print ("No se puede por que hay una o mas letras")
else:
    numero1 = int(numero1)
    numero2 = int(numero2)
    if numero1 > numero2:
        control1 = (numero2)
        control2 = (numero1+1)
    else:
        control1 = (numero1)
        control2 = (numero2+1)
    print (f"limite inferior: {control1}")

    print (list(range(control1, control2))) # Esta es una forma de imprimir un rango en forma de lista para imprimir varios numeros de una sola tacada
    for control1 in range(control1, control2):  # O de esta forma se puede imprimir por medio de un bucle o iterancia que imprima cada vez que de la vuelta.
        print (control1)

    print (f"limite inferior: {control1}")
